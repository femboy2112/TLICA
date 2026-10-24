#!/usr/bin/env python3
"""GitHub Markdown math-rendering compatibility checker for the TLICA archive.

WHAT THIS IS -- AND IS NOT
--------------------------
GitHub renders ``$...$`` / ``$$...$$`` / fenced ```` ```math ```` through MathJax on
Markdown files, PRs, issues, discussions, and wikis. This script is a STATIC,
Markdown-aware scanner that approximates GitHub's math *tokenization* closely enough to
catch the breakages that have actually bitten TLICA -- most of all ``\\operatorname``,
which the author repeatedly finds broken through this project's GitHub pipeline. It is a
necessary gate, not a sufficient proof: **a clean run here does not prove a formula
renders.** The only proof of rendering is a human (or a browser) looking at the rendered
GitHub page. Where this passes but a rendered view has not been inspected, the honest
status is UNVERIFIED. A passing Pandoc/PDF build is likewise not evidence of GitHub
rendering.

It is deliberately NOT a full CommonMark parser (the archive is stdlib-only). It tracks
fenced code/math blocks, inline code spans, the ``$`...`$`` collision-safe form, inline
``$...$`` and display ``$$`` math, and ``\\(...\\)`` / ``\\[...\\]`` legacy delimiters --
enough to avoid flagging math-looking text that is really source, and to avoid treating
currency ``$`` as a math opener. Its heuristic boundaries are documented at each rule.

TIERS (path -> how strict)
  FRONT     reader front-ends -- README.md, CITATION.md, docs/**, current foundation
            files, applications/** -- every rule at full strictness.
  RESEARCH  research/** dossiers -- hard breakers (``\\operatorname``, unclosed display)
            are errors; legacy ``\\(...\\)`` delimiters are a warning (tolerated by the
            archive's established research-tier precedent), brace heuristics informational.
  ARCHIVE   preserved/byte-frozen material -- foundation/previous_*/**, **/originals/**,
            **/history/**, **/source_prompts/**, **/journal_build/**, *VERBATIM* files --
            everything advisory (reported, never fails the gate).

EXIT STATUS
  0  no ERROR-severity findings in the scanned set (strict mode), or --advisory given
  1  at least one ERROR-severity finding (strict mode, the default)

Pure standard library: no third-party dependencies, no network.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# Trees that are never archive source. The fixtures dir and the GitHub-math
# calibration kit are skipped in a repo-wide scan (they deliberately contain broken
# macros and cross-surface edge cases -- the operatorname A/B probe, the table-pipe
# hazard strip -- for self-tests and calibration) but are scannable when a path under
# them is passed explicitly.
SKIP_DIRS = {".git", "build", "output"}
FIXTURES_DIR = REPO / "scripts" / "github_math_fixtures"
CALIBRATION_DIR = REPO / "docs" / "github-math"
_SKIP_TREES = (FIXTURES_DIR, CALIBRATION_DIR)

# --- tier classification -------------------------------------------------------------

_ARCHIVE_MARKERS = ("/previous_v", "/originals/", "/history/", "/source_prompts/",
                    "/journal_build/", "verbatim")


def classify_tier(rel: str) -> str:
    low = rel.lower()
    if any(m in low for m in _ARCHIVE_MARKERS):
        return "ARCHIVE"
    if low.startswith("research/"):
        return "RESEARCH"
    return "FRONT"


# --- rule -> severity by tier --------------------------------------------------------
# severities: 2 = ERROR, 1 = WARN, 0 = INFO
SEV_NAME = {2: "ERROR", 1: "WARN", 0: "INFO"}

# Research dossiers are PRESERVED manuscripts, not active reader front-ends: the plan
# calls them advisory. So the two "house-style" rules (operatorname, legacy delimiters)
# are WARN on RESEARCH -- reported loudly, never failing the gate -- while a genuinely
# unclosed display block stays an error anywhere, since it breaks rendering outright.
RULES = {
    "GH-OPERATORNAME":    {"FRONT": 2, "RESEARCH": 1, "ARCHIVE": 0},
    "GH-LEGACY-DELIM":    {"FRONT": 2, "RESEARCH": 1, "ARCHIVE": 0},
    "GH-UNCLOSED-DISPLAY":{"FRONT": 2, "RESEARCH": 2, "ARCHIVE": 1},
    # a lone '='/'-' line inside a $$ block is read by GitHub as a SETEXT heading
    # underline -- it turns the line above into <h1>/<h2> and shatters the math block
    # (observed on the rendered repo). A hard breaker: error on live tiers.
    "GH-SETEXT-SHATTER":  {"FRONT": 2, "RESEARCH": 2, "ARCHIVE": 1},
    "GH-INLINE-DOLLAR":   {"FRONT": 1, "RESEARCH": 1, "ARCHIVE": 0},
    "GH-BRACE-IMBALANCE": {"FRONT": 1, "RESEARCH": 0, "ARCHIVE": 0},
}

RULE_MSG = {
    "GH-OPERATORNAME": "\\operatorname is unreliable through this repo's GitHub math "
                       "pipeline; use \\mathrm{...} / \\text{...} (or \\arg\\max etc.), "
                       "verifying spacing and limit placement",
    "GH-LEGACY-DELIM": "legacy TeX math delimiter \\(...\\) / \\[...\\]; GitHub's "
                       "documented forms are $...$ and $$...$$ -- verify on a rendered page",
    "GH-UNCLOSED-DISPLAY": "display-math $$ block opened but not closed in this file",
    "GH-SETEXT-SHATTER": "a lone '='/'-' line inside a $$ block is parsed as a setext "
                         "heading underline and shatters the math block; merge the "
                         "operator onto an adjacent line (e.g. 'W\\n=' -> 'W =')",
    "GH-INLINE-DOLLAR": "possible unclosed inline $...$ math (a lone $ followed by a "
                        "math-like token with no closing $)",
    "GH-BRACE-IMBALANCE": "unbalanced { } inside an inline math span",
}


class Finding:
    __slots__ = ("rel", "line", "sev", "rule", "detail")

    def __init__(self, rel, line, sev, rule, detail=""):
        self.rel, self.line, self.sev, self.rule, self.detail = rel, line, sev, rule, detail

    def format(self):
        base = f"{self.rel}:{self.line}  [{SEV_NAME[self.sev]} {self.rule}] {RULE_MSG[self.rule]}"
        return base + (f"\n      -> {self.detail}" if self.detail else "")


# --- line tokenizer ------------------------------------------------------------------
# Segment kinds: "prose", "code", "math". We walk the characters once so that math-looking
# text inside code never reaches a math rule, and currency $ never opens math.

def tokenize_inline(line: str):
    """Yield (kind, text) segments for a single non-fence, non-display line."""
    segs = []
    n = len(line)
    i = 0
    prose_start = 0

    def flush_prose(end):
        if end > prose_start:
            segs.append(("prose", line[prose_start:end]))

    while i < n:
        c = line[i]
        if c == "\\" and i + 1 < n:
            # escaped char stays prose (\$ literal dollar, \( \) \[ \] handled by the
            # legacy-delim rule scanning prose text). Consume the pair.
            i += 2
            continue
        if c == "$":
            # dollar-backtick collision-safe math:  $`...`$
            if i + 1 < n and line[i + 1] == "`":
                j = i + 1
                while j < n and line[j] == "`":
                    j += 1
                ticks = j - (i + 1)
                close = line.find("`" * ticks + "$", j)
                if close != -1:
                    flush_prose(i)
                    segs.append(("math", line[j:close]))
                    i = close + ticks + 1
                    prose_start = i
                    continue
            # plain inline $...$ : find the next UNescaped $
            k = i + 1
            while k < n:
                if line[k] == "\\":
                    k += 2
                    continue
                if line[k] == "$":
                    break
                k += 1
            if k < n and line[k] == "$":
                flush_prose(i)
                segs.append(("math", line[i + 1:k]))
                i = k + 1
                prose_start = i
                continue
            # no closing $ -> lone dollar; mark prose, let the parity rule judge it
            i += 1
            continue
        if c == "`":
            j = i
            while j < n and line[j] == "`":
                j += 1
            ticks = j - i
            close = line.find("`" * ticks, j)
            if close != -1:
                flush_prose(i)
                segs.append(("code", line[j:close]))
                i = close + ticks
                prose_start = i
                continue
            i = j
            continue
        i += 1
    flush_prose(n)
    return segs


_LONE_DOLLAR_MATHY = re.compile(r"(?<!\\)\$[\\A-Za-z{]")  # $ immediately followed by a math-ish token
_LEGACY = re.compile(r"\\[\(\)\[\]]")
_SETEXT_LINE = re.compile(r"(?:=+|-+)")  # a pure setext-underline run (inside $$ only)


def scan_math_text(rel, lineno, tier, text, findings, check_braces):
    if "\\operatorname" in text:
        findings.append(Finding(rel, lineno, RULES["GH-OPERATORNAME"][tier],
                                 "GH-OPERATORNAME", text.strip()[:80]))
    if check_braces and text.count("{") != text.count("}"):
        findings.append(Finding(rel, lineno, RULES["GH-BRACE-IMBALANCE"][tier],
                                 "GH-BRACE-IMBALANCE", text.strip()[:80]))


def scan_file(rel: str, text: str, tier: str):
    findings = []
    lines = text.split("\n")
    in_code_fence = False
    fence_char = ""
    fence_is_math = False
    in_display = False
    display_open_line = 0

    fence_re = re.compile(r"^(\s*)(`{3,}|~{3,})(.*)$")

    for idx, raw in enumerate(lines, 1):
        stripped = raw.strip()

        if in_code_fence:
            m = fence_re.match(raw)
            if m and m.group(2)[0] == fence_char and m.group(3).strip() == "":
                in_code_fence = False
                continue
            if fence_is_math:
                scan_math_text(rel, idx, tier, raw, findings, check_braces=False)
            continue

        m = fence_re.match(raw)
        if m:
            in_code_fence = True
            fence_char = m.group(2)[0]
            fence_is_math = (m.group(3).strip().lower() == "math")
            continue

        # standalone display toggle (TLICA's dominant display style: $$ on its own line)
        if stripped == "$$":
            in_display = not in_display
            if in_display:
                display_open_line = idx
            continue

        if in_display:
            core = raw.strip()
            if core and _SETEXT_LINE.fullmatch(core):
                findings.append(Finding(rel, idx, RULES["GH-SETEXT-SHATTER"][tier],
                                        "GH-SETEXT-SHATTER", core[:80]))
            scan_math_text(rel, idx, tier, raw, findings, check_braces=False)
            continue

        # a line carrying inline $$...$$ (rare in TLICA): scan whole line for the hard
        # breaker only, skip the delicate heuristics to avoid false positives.
        if "$$" in raw:
            if "\\operatorname" in raw and "`" not in raw:
                findings.append(Finding(rel, idx, RULES["GH-OPERATORNAME"][tier],
                                        "GH-OPERATORNAME", stripped[:80]))
            continue

        segs = tokenize_inline(raw)
        for kind, seg_text in segs:
            if kind == "math":
                scan_math_text(rel, idx, tier, seg_text, findings, check_braces=True)
            elif kind == "prose":
                if _LEGACY.search(seg_text):
                    findings.append(Finding(rel, idx, RULES["GH-LEGACY-DELIM"][tier],
                                            "GH-LEGACY-DELIM", seg_text.strip()[:80]))
                if "\\operatorname" in seg_text:
                    findings.append(Finding(rel, idx, RULES["GH-OPERATORNAME"][tier],
                                            "GH-OPERATORNAME", seg_text.strip()[:80]))
                # unclosed-inline heuristic: a lone $ directly before a math-ish token,
                # with no closing $ (currency "$100" / "$ 5" is skipped by the regex).
                if _LONE_DOLLAR_MATHY.search(seg_text):
                    findings.append(Finding(rel, idx, RULES["GH-INLINE-DOLLAR"][tier],
                                            "GH-INLINE-DOLLAR", seg_text.strip()[:80]))

    if in_display:
        findings.append(Finding(rel, display_open_line,
                                RULES["GH-UNCLOSED-DISPLAY"][tier],
                                "GH-UNCLOSED-DISPLAY", "display block never closed"))
    return findings


# --- driver --------------------------------------------------------------------------

def iter_targets(paths):
    for p in paths:
        p = Path(p)
        if p.is_dir():
            for md in sorted(p.rglob("*.md")):
                if SKIP_DIRS & set(md.parts):
                    continue
                # skip the fixtures tree and the calibration kit in a directory sweep
                skip = False
                for tree in _SKIP_TREES:
                    try:
                        md.resolve().relative_to(tree)
                        skip = True
                        break
                    except ValueError:
                        pass
                if skip:
                    continue
                yield md
        elif p.suffix == ".md":
            yield p


def main(argv=None):
    ap = argparse.ArgumentParser(description="GitHub Markdown math compatibility checker.")
    ap.add_argument("paths", nargs="*", help="files or dirs (default: whole repo)")
    ap.add_argument("--advisory", action="store_true",
                    help="report everything but always exit 0 (survey mode)")
    ap.add_argument("--min-severity", choices=["info", "warn", "error"], default="info",
                    help="only print findings at or above this severity (default: info)")
    args = ap.parse_args(argv)

    targets = list(iter_targets(args.paths or [REPO]))
    min_sev = {"info": 0, "warn": 1, "error": 2}[args.min_severity]

    all_findings = []
    for md in targets:
        try:
            rel = str(md.resolve().relative_to(REPO))
        except ValueError:
            rel = str(md)
        tier = classify_tier(rel)
        try:
            text = md.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        all_findings.extend(scan_file(rel, text, tier))

    shown = [f for f in all_findings if f.sev >= min_sev]
    errors = [f for f in all_findings if f.sev == 2]
    warns = [f for f in all_findings if f.sev == 1]

    shown.sort(key=lambda f: (-f.sev, f.rel, f.line))
    for f in shown:
        print("  " + f.format(), file=sys.stderr if f.sev == 2 else sys.stdout)

    print(f"check_github_math: scanned {len(targets)} files -- "
          f"{len(errors)} error(s), {len(warns)} warning(s), "
          f"{len(all_findings) - len(errors) - len(warns)} info "
          f"(STATIC scan; rendered GitHub view is UNVERIFIED here)")
    if errors and not args.advisory:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
