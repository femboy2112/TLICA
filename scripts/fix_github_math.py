#!/usr/bin/env python3
"""Convert GitHub-incompatible LaTeX math to GitHub's documented MathJax forms.

WHY
---
GitHub renders math only through ``$...$`` / ``$$...$$`` / fenced ```` ```math ````.
The legacy TeX delimiters ``\\(...\\)`` and ``\\[...\\]`` are NOT recognized -- they
leak through as literal backslash-paren text (observed on the rendered repo) -- and
``\\operatorname`` is rejected by GitHub's MathJax configuration. This tool rewrites
those three constructs to the supported, meaning-preserving forms:

    \\(x\\)              -> $x$
    \\[ ... \\]          -> $$ ... $$     (standalone delimiter lines, blockquote-aware)
    \\operatorname{F}    -> \\mathrm{F}           (non-star: same glyph, same meaning)
    \\operatorname*{F}   -> \\mathop{\\mathrm{F}}  (star: keeps under-limit placement)

SAFETY
------
This is the companion *fixer* to ``check_github_math.py`` and shares its tokenizer
semantics so the two never disagree about what is code vs prose vs math. It is
surgical by construction:

  * Fenced code blocks (``` / ~~~) are copied VERBATIM -- never rewritten. A fenced
    block tagged ```` ```math ```` gets only the ``\\operatorname`` swap (it is math).
  * Inline code spans (`` `...` ``, `` $`...`$ ``) are preserved VERBATIM -- so prose
    that *describes* ``\\operatorname`` or ``\\(`` in backticks is left intact.
  * Only a BALANCED inline ``\\(...\\)`` / ``\\[...\\]`` pair is converted; a bare
    ``\\\\[4pt]`` matrix row-break (backslash-escaped) is never matched.
  * ``\\[`` / ``\\]`` are converted as display delimiters only when they are alone on
    their line (optionally behind a ``>`` blockquote prefix), matching the archive's
    dominant ``$$``-on-its-own-line style.
  * The transform is idempotent: running it on already-converted text is a no-op.

It does NOT prove anything renders -- that still needs a human on the rendered page.
Pure standard library.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKIP_DIRS = {".git", "build", "output"}
FIXTURES_DIR = REPO / "scripts" / "github_math_fixtures"

# Byte-frozen / verbatim trees are never rewritten.
_ARCHIVE_MARKERS = ("/previous_v", "/originals/", "/history/", "/source_prompts/",
                    "/journal_build/", "verbatim")


def is_archive(rel: str) -> bool:
    return any(m in rel.lower() for m in _ARCHIVE_MARKERS)


_FENCE_RE = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")
_DISPLAY_OPEN = re.compile(r"^(\s*(?:>\s*)*)\\\[\s*$")
_DISPLAY_CLOSE = re.compile(r"^(\s*(?:>\s*)*)\\\]\s*$")
_DOLLAR_DISPLAY = re.compile(r"^(\s*(?:>\s*)*)\$\$\s*$")

_OPNAME_STAR = re.compile(r"\\operatorname\*\s*\{([^{}]*)\}")
_OPNAME = re.compile(r"\\operatorname\s*\{([^{}]*)\}")
# balanced inline pairs; the (?<!\\) guard keeps \\( and \\[4pt] (escaped) untouched.
_INLINE_PAREN = re.compile(r"(?<!\\)\\\((.*?)(?<!\\)\\\)")
_INLINE_BRACK = re.compile(r"(?<!\\)\\\[(.*?)(?<!\\)\\\]")


def swap_operatorname(s: str) -> str:
    s = _OPNAME_STAR.sub(r"\\mathop{\\mathrm{\1}}", s)
    s = _OPNAME.sub(r"\\mathrm{\1}", s)
    return s


def segment_line(line: str):
    """Lossless split into (kind, text) where text INCLUDES its delimiters.

    kind in {'code','math','prose'}. Mirrors check_github_math.tokenize_inline but
    preserves delimiters so the line can be reassembled byte-for-byte.
    """
    segs = []
    n = len(line)
    i = 0
    start = 0

    def flush(end):
        if end > start:
            segs.append(("prose", line[start:end]))

    while i < n:
        c = line[i]
        if c == "\\" and i + 1 < n:
            i += 2
            continue
        if c == "`":
            j = i
            while j < n and line[j] == "`":
                j += 1
            ticks = j - i
            close = line.find("`" * ticks, j)
            if close != -1:
                flush(i)
                segs.append(("code", line[i:close + ticks]))
                i = close + ticks
                start = i
                continue
            i = j
            continue
        if c == "$":
            if i + 1 < n and line[i + 1] == "`":
                j = i + 1
                while j < n and line[j] == "`":
                    j += 1
                ticks = j - (i + 1)
                close = line.find("`" * ticks + "$", j)
                if close != -1:
                    flush(i)
                    segs.append(("math", line[i:close + ticks + 1]))
                    i = close + ticks + 1
                    start = i
                    continue
            k = i + 1
            while k < n:
                if line[k] == "\\":
                    k += 2
                    continue
                if line[k] == "$":
                    break
                k += 1
            if k < n and line[k] == "$":
                flush(i)
                segs.append(("math", line[i:k + 1]))
                i = k + 1
                start = i
                continue
            i += 1
            continue
        i += 1
    flush(n)
    return segs


def convert_prose(seg: str) -> str:
    seg = _INLINE_PAREN.sub(r"$\1$", seg)
    seg = _INLINE_BRACK.sub(r"$$\1$$", seg)
    seg = swap_operatorname(seg)
    return seg


def convert_line(line: str) -> str:
    out = []
    for kind, text in segment_line(line):
        if kind == "code":
            out.append(text)                       # verbatim
        elif kind == "math":
            out.append(swap_operatorname(text))    # existing $...$ : opname only
        else:
            out.append(convert_prose(text))
    return "".join(out)


_SETEXT = re.compile(r"(?:=+|-+)")          # a pure setext-underline run
_BQ_STRIP = re.compile(r"^[>\s]*")          # leading blockquote markers + ws (no nested quantifier)
_DISPLAY_ANY = re.compile(r"^(\s*(?:>\s*)*)\$\$\s*$")


def fix_setext_in_display(lines):
    """Merge a lone '='/'-' line inside a $$ block onto the previous content line.

    GitHub parses a line of pure '=' or '-' as a SETEXT HEADING underline, which
    turns the line above into an <h1>/<h2> and orphans the surrounding $$ delimiters
    -- observed shattering the W_t block on the rendered repo. Merging the operator
    up ("W_t\\n=" -> "W_t =") is identical math (newlines are whitespace in TeX) and
    removes the trigger. Fences are skipped; blockquote prefixes are preserved.
    """
    out = []
    in_fence = False
    fence_char = ""
    in_display = False
    changes = 0
    fence_re = _FENCE_RE
    for raw in lines:
        if in_fence:
            m = fence_re.match(raw)
            if m and m.group(2)[0] == fence_char and m.group(3).strip() == "":
                in_fence = False
            out.append(raw)
            continue
        m = fence_re.match(raw)
        if m:
            in_fence = True
            fence_char = m.group(2)[0]
            out.append(raw)
            continue
        if _DISPLAY_ANY.match(raw):
            in_display = not in_display
            out.append(raw)
            continue
        if in_display:
            core = _BQ_STRIP.sub("", raw).rstrip()
            if core and _SETEXT.fullmatch(core) and out and not _DISPLAY_ANY.match(out[-1]):
                out[-1] = out[-1].rstrip() + " " + core
                changes += 1
                continue
        out.append(raw)
    return out, changes


def convert_text(text: str):
    """Return (new_text, nchanges_estimate). Line-structure preserved."""
    lines = text.split("\n")
    out = []
    in_fence = False
    fence_char = ""
    fence_is_math = False
    in_display = False
    changes = 0

    for raw in lines:
        if in_fence:
            m = _FENCE_RE.match(raw)
            if m and m.group(2)[0] == fence_char and m.group(3).strip() == "":
                in_fence = False
                out.append(raw)
                continue
            out.append(swap_operatorname(raw) if fence_is_math else raw)
            continue

        m = _FENCE_RE.match(raw)
        if m:
            in_fence = True
            fence_char = m.group(2)[0]
            fence_is_math = (m.group(3).strip().lower() == "math")
            out.append(raw)
            continue

        if in_display:
            # inside a display block (opened by $$ or a converted \[): close on \] or $$
            mc = _DISPLAY_CLOSE.match(raw)
            if mc:
                out.append(mc.group(1) + "$$")
                in_display = False
                changes += 1
                continue
            if _DOLLAR_DISPLAY.match(raw):
                out.append(raw)
                in_display = False
                continue
            out.append(swap_operatorname(raw))
            continue

        mo = _DISPLAY_OPEN.match(raw)
        if mo:
            out.append(mo.group(1) + "$$")
            in_display = True
            changes += 1
            continue
        if _DOLLAR_DISPLAY.match(raw):
            out.append(raw)
            in_display = True
            continue

        new = convert_line(raw)
        if new != raw:
            changes += 1
        out.append(new)

    # second pass: remove setext-underline shatter inside display blocks
    out, setext_changes = fix_setext_in_display(out)
    return "\n".join(out), changes + setext_changes


def iter_targets(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            for md in sorted(p.rglob("*.md")):
                if SKIP_DIRS & set(md.parts):
                    continue
                try:
                    md.resolve().relative_to(FIXTURES_DIR)
                    continue
                except ValueError:
                    pass
                yield md
        elif p.suffix == ".md":
            yield p


def main(argv=None):
    ap = argparse.ArgumentParser(description="Convert legacy LaTeX math to GitHub forms.")
    ap.add_argument("paths", nargs="*", help="files or dirs (default: whole repo)")
    ap.add_argument("--apply", action="store_true", help="write changes (default: dry run)")
    ap.add_argument("--include-archive", action="store_true",
                    help="also rewrite byte-frozen archive/verbatim trees (off by default)")
    args = ap.parse_args(argv)

    targets = list(iter_targets(args.paths or [REPO]))
    touched = 0
    total_changes = 0
    for md in targets:
        try:
            rel = str(md.resolve().relative_to(REPO))
        except ValueError:
            rel = str(md)
        if not args.include_archive and is_archive(rel):
            continue
        try:
            text = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        new, changes = convert_text(text)
        if new != text:
            touched += 1
            total_changes += changes
            if args.apply:
                md.write_text(new, encoding="utf-8")
                print(f"  fixed  {rel}  (~{changes} line-changes)")
            else:
                print(f"  would-fix  {rel}  (~{changes} line-changes)")

    verb = "fixed" if args.apply else "would fix"
    print(f"fix_github_math: {verb} {touched} file(s), ~{total_changes} line-changes "
          f"({'APPLIED' if args.apply else 'DRY RUN -- rerun with --apply'})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
