#!/usr/bin/env python3
"""Semantic-drift gate for the TLICA archive.

TLICA is a philosophical framework built *using* mathematics, so it constantly
borrows math/physics-general words -- "field", "projection", "phase", "basis",
"topology", "gauge" -- and reuses them in a specific technical sense. Each such
word arrives in a math-literate reader's head already meaning something else
(an algebraic field, a linear-algebra basis, an oscillator's phase). Left
unpinned and untagged, one word ends up carrying several meanings at once: the
worked case is "field", which in the archive means *reality*, *your view of
reality*, *your choice-space*, and *the filter mechanism over it* -- a scope
ladder -- and even the glossary uses it in three senses without saying which.
That is the drift this gate exists to catch, the semantic sibling of the LaTeX
intake hygiene the archive already enforces.

The rule this gate enforces: every borrowed term on the watchlist
(``scripts/math_terms.txt``) that is *common* in the theory corpus must have a
dedicated pinning entry in ``docs/glossary.md`` -- an entry whose title LEADS
with the term (``**Field** -- ...`` / ``**Asymptotic layer** -- ...``), not a
mere mention buried in prose or in a compound like ``**delta-extended field**``.
A dedicated pin is where the TLICA sense gets stated and the off-the-shelf math
sense gets fenced; the human terminology sweep then keeps each *use* tagged to
the right scope. This gate checks *presence of the pin*, which it can do
mechanically; it does not certify the pin's scope-discipline, which it cannot.

Watchlist tokens are word-start stems matched case-insensitively (so ``topolog``
catches "topology" and "topological"). A term is counted across the theory
corpus (``applications/``, ``foundation/``, ``research/``); the glossary is the
pin registry. A term FAILS the gate when it is used at least ``THRESHOLD`` times
and has no dedicated glossary entry.

Exit status:
    0  every common watched term is pinned (or none are common)
    1  at least one common watched term lacks a dedicated glossary pin
    2  a usage error (missing watchlist or glossary)

Pure standard library: no third-party dependencies, no network.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
WATCHLIST = REPO / "scripts" / "math_terms.txt"
GLOSSARY = REPO / "docs" / "glossary.md"

# Directories that hold the *theory* prose (where drift bites). The wiki under
# docs/ is deliberately excluded: it is plain-language translation, and its
# glossary is the pin registry, not a usage site to police.
SCAN_DIRS = ("applications", "foundation", "research")

# A watched term must be pinned once it is used at least this many times. Below
# it, the term is reported for visibility but does not fail the gate -- an
# incidental one-off (e.g. a stray "vector") should not force a glossary entry.
THRESHOLD = 6

# A dedicated glossary entry -- prose ``**Title** -- ...`` or a symbol-table row
# ``| **Title** | ...`` -- from which we read the leading title.
_PROSE_ENTRY = re.compile(r"^\*\*(?P<title>[^*]+)\*\*")
_TABLE_ENTRY = re.compile(r"^\|\s*\*\*(?P<title>[^*]+)\*\*")
_LEADING_ARTICLE = re.compile(r"^(?:the|a|an)\s+")


def load_watchlist() -> list[tuple[str, str]]:
    """Return [(stem, note)] from the watchlist, in file order."""
    terms: list[tuple[str, str]] = []
    for raw in WATCHLIST.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        stem, _, note = line.partition("#")
        terms.append((stem.strip().lower(), note.strip()))
    return terms


def glossary_entry_titles() -> list[str]:
    """Every dedicated glossary entry's leading title, lowercased & de-articled."""
    titles: list[str] = []
    for line in GLOSSARY.read_text(encoding="utf-8").splitlines():
        m = _PROSE_ENTRY.match(line) or _TABLE_ENTRY.match(line)
        if not m:
            continue
        title = _LEADING_ARTICLE.sub("", m.group("title").strip().lower())
        titles.append(title)
    return titles


def is_pinned(stem: str, titles: list[str]) -> bool:
    """True when some entry's title LEADS with the term stem as a word start.

    Leading-with is the discriminator: a dedicated entry names its term at the
    front ("Field --", "Asymptotic layer --"), whereas a compound that merely
    contains the word ("delta-extended field") leads with its qualifier and is a
    pin for the *compound*, not for the bare term.
    """
    pat = re.compile(r"^" + re.escape(stem))
    return any(pat.match(title) for title in titles)


def count_uses(stem: str) -> int:
    """Case-insensitive word-start occurrences of the stem in the theory corpus."""
    pat = re.compile(r"\b" + re.escape(stem), re.IGNORECASE)
    total = 0
    for d in SCAN_DIRS:
        root = REPO / d
        if not root.is_dir():
            continue
        for md in root.rglob("*.md"):
            if ".git" in md.parts:
                continue
            try:
                total += len(pat.findall(md.read_text(encoding="utf-8")))
            except UnicodeDecodeError:
                continue
    return total


def main() -> int:
    if not WATCHLIST.is_file():
        print(f"check_math_terms: missing watchlist {WATCHLIST}", file=sys.stderr)
        return 2
    if not GLOSSARY.is_file():
        print(f"check_math_terms: missing glossary {GLOSSARY}", file=sys.stderr)
        return 2

    terms = load_watchlist()
    titles = glossary_entry_titles()

    rows = []
    for stem, note in terms:
        uses = count_uses(stem)
        pinned = is_pinned(stem, titles)
        failing = uses >= THRESHOLD and not pinned
        rows.append((stem, uses, pinned, failing, note))
    rows.sort(key=lambda r: r[1], reverse=True)

    width = max((len(r[0]) for r in rows), default=4)
    print(f"{'TERM':<{width}}  {'USES':>5}  {'PINNED':>6}  VERDICT")
    print(f"{'-' * width}  {'-' * 5:>5}  {'-' * 6:>6}  -------")
    for stem, uses, pinned, failing, note in rows:
        if failing:
            verdict = "NEEDS PIN"
        elif uses < THRESHOLD:
            verdict = "ok (rare)"
        else:
            verdict = "ok"
        print(f"{stem:<{width}}  {uses:>5}  {'yes' if pinned else 'no':>6}  {verdict}")

    failures = [r for r in rows if r[3]]
    if failures:
        print(
            f"\nDRIFT RISK: {len(failures)} common watched term(s) lack a "
            f"dedicated glossary pin",
            file=sys.stderr,
        )
        for stem, uses, _pinned, _failing, note in failures:
            hint = f' -- add "**{stem}...** -- ..." to docs/glossary.md'
            print(f"  {stem} ({uses} uses){hint}", file=sys.stderr)
            if note:
                print(f"      note: {note}", file=sys.stderr)
        print(
            "\n  (Pin = state the TLICA sense and fence the math/physics one. "
            "The gate checks the pin exists; the terminology sweep keeps each "
            "USE tagged to the right scope.)",
            file=sys.stderr,
        )
        return 1

    print(
        f"\nPASS check_math_terms: every watched term used >= {THRESHOLD} times "
        f"is pinned in the glossary ({len(terms)} watched, {len(titles)} entries)"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
