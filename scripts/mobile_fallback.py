#!/usr/bin/env python3
r"""Source-matched MathJax PNG snapshots for GitHub's Android app.

GitHub's Android app renders no live MathJax, so a repo reader on the app sees raw
``$...$`` source. This builds PNG fallbacks for the *few* pages that matter, each
image rendered from an authoritative source and pinned to a SHA-256 of that source
so the picture can never silently drift from the equation it depicts. It is NOT a
repo-wide image mirror: the 100+ research dossiers stay native (they render on
desktop and mobile web).

Two decks share one engine (adapted from Leah's SMPTeX ``mobile_fallback.py``):

  calibration  the SMPTeX T00-T21 calibration strips, parsed from
               docs/github-math/GITHUB_MATH_TEST_CARD.md, imaged to assets/mobile/.
  tlica        TLICA's load-bearing equations, EXTRACTED from the real source files
               named in docs/github-math/mobile-math.sources.json (never retyped),
               imaged to assets/mobile-tlica/, and written up as
               docs/github-math/MOBILE_APP_FALLBACK_TLICA.md.

Default run (stdlib only) VERIFIES committed images against their sources; ``--build``
regenerates them and needs Node + mathjax-full, CairoSVG, and Pillow.

Usage:
  python3 scripts/mobile_fallback.py [--deck calibration|tlica|all]            # verify
  python3 scripts/mobile_fallback.py --build [--deck calibration|tlica|all]   # regenerate
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CARD = ROOT / "docs/github-math/GITHUB_MATH_TEST_CARD.md"
SPEC = ROOT / "docs/github-math/mobile-math.sources.json"
RENDERER = ROOT / "scripts/render_mathjax_svg.cjs"
PNG_HEADER = b"\x89PNG\r\n\x1a\n"

HEAD = re.compile(r"^## (T\d\d) · (.+)$", re.M)
FENCE = re.compile(r"^```math\s*\n(.*?)\n```", re.M | re.S)
DISPLAY = re.compile(r"^\$\$\s*\n(.*?)\n\$\$", re.M | re.S)
PROTECTED = re.compile(r"\$`([^\n]+?)`\$")
INLINE = re.compile(r"(?<!\$)\$(?!\$|`)([^\n$]+?)\$(?!\$)")

DECKS = {
    "calibration": {
        "assets": ROOT / "assets/mobile",
        "manifest": ROOT / "assets/mobile/manifest.json",
        "renderer": "MathJax 3 SVG -> CairoSVG/Pillow PNG",
        "scope": "Static reference, not native GitHub Android math certification",
    },
    "tlica": {
        "assets": ROOT / "assets/mobile-tlica",
        "manifest": ROOT / "assets/mobile-tlica/manifest.json",
        "renderer": "MathJax 3 SVG -> CairoSVG/Pillow PNG",
        "scope": "Static reference projected from TLICA source files; not a render certificate",
    },
}


def digest(parts) -> str:
    return hashlib.sha256(
        json.dumps(parts, ensure_ascii=False, separators=(",", ":")).encode()
    ).hexdigest()


def mobile_lines(source: str) -> list[str]:
    """Reflow an equation at presentation-spacing boundaries for narrow screens."""
    return [part.strip() for part in source.split(r"\qquad") if part.strip()]


# --- source extraction --------------------------------------------------------------

def _display_blocks(text: str) -> list[str]:
    """Every display-math block in a Markdown file: multi-line $$, ```math, and
    single-line (optionally blockquote-prefixed) $$ ... $$."""
    blocks: list[str] = []
    blocks += [m.group(1).strip() for m in FENCE.finditer(text)]
    blocks += [m.group(1).strip() for m in DISPLAY.finditer(text)]
    for line in text.splitlines():
        s = line.strip()
        while s.startswith(">"):
            s = s[1:].strip()
        if s.startswith("$$") and s.endswith("$$") and len(s) > 4:
            blocks.append(s[2:-2].strip())
    return blocks


def extract(source_file: Path, match: str) -> str:
    """Return the TeX of the single display block in `source_file` that contains
    `match`. Raise if zero or more than one match -- never guess."""
    text = source_file.read_text(encoding="utf-8")
    hits = [b for b in _display_blocks(text) if match in b]
    if not hits:
        raise ValueError(f"no display block containing {match!r} in {source_file}")
    uniq = sorted(set(hits))
    if len(uniq) > 1:
        raise ValueError(f"ambiguous match {match!r} in {source_file}: {len(uniq)} distinct blocks")
    return uniq[0]


def strips_calibration() -> list[dict]:
    text = CARD.read_text(encoding="utf-8")
    markers = list(HEAD.finditer(text))
    result = []
    for i, match in enumerate(markers):
        end = markers[i + 1].start() if i + 1 < len(markers) else len(text)
        body = text[match.end():end]
        body = re.split(r"^\s*---\s*$|^## ", body, maxsplit=1, flags=re.M)[0]
        expr = []
        for rule in (FENCE, DISPLAY, PROTECTED):
            body = rule.sub(lambda m: (expr.append(m.group(1).strip()) or "\n"), body)
        body = re.sub(r"<span>\$</span>", "", body)
        body = re.sub(r"`[^`\n]*`", "", body)
        expr += [m.group(1).strip() for m in INLINE.finditer(body)]
        if not expr:
            raise ValueError("Missing live TeX in " + match.group(1))
        result.append({"id": match.group(1), "title": match.group(2), "tex": expr})
    if [x["id"] for x in result] != [f"T{i:02}" for i in range(22)]:
        raise ValueError("Expected T00 through T21, in order")
    return result


def equations_tlica() -> list[dict]:
    spec = json.loads(SPEC.read_text(encoding="utf-8"))
    out = []
    for e in spec["equations"]:
        src = ROOT / e["file"]
        tex = extract(src, e["match"])
        out.append({"id": e["id"], "title": e["title"], "file": e["file"],
                    "match": e["match"], "tex": [tex]})
    ids = [x["id"] for x in out]
    if len(ids) != len(set(ids)):
        raise ValueError("duplicate equation id in spec")
    return out


def values_for(deck: str) -> list[dict]:
    return strips_calibration() if deck == "calibration" else equations_tlica()


# --- verify (stdlib only) -----------------------------------------------------------

def check(deck: str) -> int:
    cfg = DECKS[deck]
    values = values_for(deck)
    if not cfg["manifest"].is_file():
        print(f"[{deck}] PNG manifest not yet generated: {cfg['manifest']}", file=sys.stderr)
        return 1
    manifest = json.loads(cfg["manifest"].read_text(encoding="utf-8"))
    found = {entry["id"]: entry for entry in manifest["entries"]}
    errors = []
    for v in values:
        rec = found.get(v["id"])
        if rec is None:
            errors.append(v["id"] + " missing record")
            continue
        if rec["tex_sha256"] != digest(v["tex"]):
            errors.append(v["id"] + " SOURCE DRIFT (equation changed; rebuild with --build)")
        asset = ROOT / rec["path"]
        if not asset.exists():
            errors.append(v["id"] + " image missing")
            continue
        raw = asset.read_bytes()
        if not raw.startswith(PNG_HEADER) or hashlib.sha256(raw).hexdigest() != rec["png_sha256"]:
            errors.append(v["id"] + " corrupted / stale image")
    if len(found) != len(values):
        errors.append(f"manifest must contain exactly {len(values)} records, has {len(found)}")
    for e in errors:
        print("ERROR", f"[{deck}]", e, file=sys.stderr)
    print(f"mobile-fallback [{deck}]: {len(values)} items, {len(errors)} findings")
    return int(bool(errors))


# --- build (needs Node + CairoSVG + Pillow) -----------------------------------------

def _render_svgs(formulas: list[str]) -> list[str]:
    env = dict(os.environ)
    node_path = os.environ.get("MOBILE_FALLBACK_NODE_PATH")
    if node_path:
        env["NODE_PATH"] = node_path
    run = subprocess.run(
        ["node", str(RENDERER)],
        input=json.dumps({"tex": formulas}),
        text=True, capture_output=True, check=False, env=env,
    )
    if run.returncode:
        print(run.stderr, file=sys.stderr)
        raise SystemExit(2)
    svgs = json.loads(run.stdout)["svg"]
    if len(svgs) != len(formulas):
        raise ValueError("SVG count mismatch")
    return svgs


def build(deck: str) -> int:
    try:
        import cairosvg
        from PIL import Image, ImageDraw, ImageFont
    except ImportError as err:
        print("Missing optional Pillow/CairoSVG: " + str(err), file=sys.stderr)
        return 2
    cfg = DECKS[deck]
    values = values_for(deck)
    formulas = [seg for v in values for item in v["tex"] for seg in mobile_lines(item)]
    svgs = _render_svgs(formulas)
    try:
        regular = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 24)
        bold = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 32)
    except OSError:
        regular = ImageFont.load_default()
        bold = regular
    cfg["assets"].mkdir(parents=True, exist_ok=True)
    records = []
    index = 0
    for v in values:
        pictures = []
        for item in v["tex"]:
            for _seg in mobile_lines(item):
                png = cairosvg.svg2png(bytestring=svgs[index].encode("utf-8"), scale=3)
                index += 1
                pic = Image.open(io.BytesIO(png)).convert("RGBA")
                if pic.width < 10 or pic.height < 10:
                    raise ValueError("Empty formula " + v["id"])
                pictures.append(pic)
        width = max(800, max(pic.width for pic in pictures) + 90)
        height = 140 + sum(max(86, pic.height) + 22 for pic in pictures)
        canvas = Image.new("RGB", (width, height), "#f7f7f4")
        draw = ImageDraw.Draw(canvas)
        draw.rectangle((0, 0, width - 1, height - 1), outline="#9fa0a5", width=2)
        draw.rectangle((0, 0, 14, height - 1), fill="#13131a")
        headline = v["id"] + "  " + v["title"]
        original = headline
        while len(headline) > 4 and draw.textlength(headline, font=bold) > width - 100:
            headline = headline[:-2]
        if headline != original:
            headline = headline.rstrip() + "…"
        draw.text((42, 22), headline, font=bold, fill="#17171c")
        subtitle = "REFERENCE IMAGE  ·  SOURCE: " + (v.get("file") or CARD.name)
        draw.text((44, 68), subtitle, font=regular, fill="#55565e")
        y = 118
        for pic in pictures:
            canvas.paste(pic, (45, y + max(0, (max(86, pic.height) - pic.height) // 2)), pic)
            y += max(86, pic.height) + 22
        target = cfg["assets"] / (v["id"].lower() + ".png")
        canvas.save(target, optimize=True)
        rec = {"id": v["id"], "title": v["title"],
               "tex_sha256": digest(v["tex"]),
               "path": target.relative_to(ROOT).as_posix(),
               "png_sha256": hashlib.sha256(target.read_bytes()).hexdigest(),
               "width": width, "height": height}
        if v.get("file"):
            rec["source_file"] = v["file"]
            rec["match"] = v["match"]
        records.append(rec)
    cfg["manifest"].parent.mkdir(parents=True, exist_ok=True)
    cfg["manifest"].write_text(
        json.dumps({"version": 1, "deck": deck,
                    "source": "docs/github-math/GITHUB_MATH_TEST_CARD.md" if deck == "calibration"
                    else "docs/github-math/mobile-math.sources.json",
                    "renderer": cfg["renderer"], "scope": cfg["scope"],
                    "entries": records}, indent=2) + "\n", encoding="utf-8")
    if deck == "tlica":
        _write_tlica_page(records)
    return check(deck)


# --- generated TLICA fallback page --------------------------------------------------

def _write_tlica_page(records: list[dict]) -> None:
    page = ROOT / "docs/github-math/MOBILE_APP_FALLBACK_TLICA.md"
    lines = [
        "# TLICA core equations — Android-app fallback 📱",
        "",
        "[← calibration kit](README.md) · [calibration strips](MOBILE_APP_FALLBACK.md) · "
        "[compatibility ledger](MATH_COMPATIBILITY_LEDGER.md)",
        "",
        "> **Why this page exists.** GitHub's Android app renders no live MathJax, so on the "
        "app the equations below would otherwise appear as raw `$…$` source. Each image is "
        "rendered from the **exact TeX in the source file named beneath it** — never retyped — "
        "and pinned to a SHA-256 of that source, so it cannot silently drift. On desktop or a "
        "mobile **web browser**, read the live theory instead; this is a fallback, not the canon.",
        "",
        "> **Boundary.** A PNG appearing on screen is **not** a passing TeX-render test, and these "
        "ten equations are a reader's entry map, not the full formal apparatus — that lives in the "
        "[foundation](../../foundation/).",
        "",
        "## The load-bearing equations",
        "",
    ]
    for rec in records:
        lines.append(f"### {rec['id']} · {rec['title']}")
        lines.append("")
        lines.append(f"![{rec['id']} — {rec['title']}](../../{rec['path']})")
        lines.append("")
        lines.append(f"*Source: [`{rec['source_file']}`](../../{rec['source_file']}).*")
        lines.append("")
    lines += [
        "## Rebuilding",
        "",
        "Verify committed images against their sources (standard library only):",
        "",
        "```bash",
        "python3 scripts/mobile_fallback.py --deck tlica",
        "```",
        "",
        "Regenerate after a source equation changes (needs Node + mathjax-full, CairoSVG, Pillow):",
        "",
        "```bash",
        "make mobile-fallback            # or: python3 scripts/mobile_fallback.py --build --deck tlica",
        "```",
        "",
        "The equation list is [`mobile-math.sources.json`](mobile-math.sources.json); each entry "
        "names a source file and a unique substring of the display block to project. Add an entry "
        "there, never retype an equation here.",
        "",
    ]
    page.write_text("\n".join(lines) + "\n", encoding="utf-8")


def main(argv=None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--build", action="store_true", help="regenerate PNGs (needs Node/CairoSVG/Pillow)")
    p.add_argument("--deck", choices=["calibration", "tlica", "all"], default="all")
    args = p.parse_args(argv)
    decks = ["calibration", "tlica"] if args.deck == "all" else [args.deck]
    rc = 0
    for deck in decks:
        rc |= (build(deck) if args.build else check(deck))
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
