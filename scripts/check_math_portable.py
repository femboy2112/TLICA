#!/usr/bin/env python3
r"""TLICA gate wrapper around SMPTeX's portable source guard.

``scripts/math_guard.py`` is vendored BYTE-PRISTINE from SMPTeX
(https://github.com/femboy2112/SMPTeX) so it can be re-vendored cleanly when
upstream changes. This wrapper -- and only this wrapper -- applies TLICA's
carve-outs, each justified in-line, and fails on everything else:

  CARVE-OUT 1 (excluded trees). ``scripts/github_math_fixtures/`` (deliberately
    broken self-test fixtures) and ``docs/github-math/`` (the calibration kit --
    the operatorname A/B probe, the table-pipe hazard strip, cross-surface edge
    cases) are not archive source and are not scanned. They remain scannable when
    a path under them is passed to math_guard.py directly.

  CARVE-OUT 2 (byte-frozen archive is advisory). Files in TLICA's frozen archive
    tiers (previous_v*/, originals/, history/, source_prompts/, journal_build/,
    verbatim) are preserved exactly as written; their findings are reported as
    advisory and never fatal. This matches scripts/check_github_math.py, whose
    classify_tier() is reused here so the two gates agree on what is frozen.

  CARVE-OUT 3 (single-line display). ``DISPLAY_DELIMITER`` fires on block math
    written as ``$$ ... $$`` on one line. GitHub's own math documentation renders
    block math on a single line (its canonical example puts the whole
    ``$$ \left( \sum ... \right) $$`` on one line), so in TLICA this is a
    portability PREFERENCE, not a render bug (verified against the GitHub docs
    2026-10-23). It is reported as advisory, never fatal. A ``$$ X $$`` single-line
    display also makes the guard emit a spurious ``BARE_TEX`` for the macros in
    ``X`` (the guard blanks only the ``$$`` tokens and treats the remainder as
    prose). That BARE_TEX is the same artifact, so it is suppressed ONLY when it
    co-occurs with a DISPLAY_DELIMITER on the exact same line; a BARE_TEX on a line
    with no ``$$`` is a genuine macro-in-prose bug and still fails.

Everything else math_guard reports in a live (FRONT/RESEARCH) file (TABLE_PIPE,
UNTERMINATED_INLINE, BRACES, ENVIRONMENT, LEFT_RIGHT, UNSAFE_MACRO/ENVIRONMENT,
UNCERTIFIED_MACRO, ALT_DELIMITER, UNTERMINATED_DISPLAY/FENCE, EMPTY_MATH) is a real
portability defect and is fatal.

Pure standard library. Exit 0 = clean (after carve-outs); 1 = real findings remain.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent


def _load(name: str):
    spec = importlib.util.spec_from_file_location(name, REPO / "scripts" / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = mod
    spec.loader.exec_module(mod)
    return mod


math_guard = _load("math_guard")
cgm = _load("check_github_math")  # reuse its tier classification

EXCLUDE_TREES = (REPO / "scripts" / "github_math_fixtures", REPO / "docs" / "github-math")
ADVISORY_CODES = {"DISPLAY_DELIMITER"}

# CARVE-OUT 2b: preservation archives and author-paused / DOI-frozen dossiers are
# advisory, exactly like the byte-frozen archive tiers (carve-out 2). We do not edit
# preserved historical drafts or paused work to satisfy a linter, and the findings
# there (a lone currency $) render as literal text on GitHub anyway -- no real breakage.
PRESERVATION_TREES = (
    REPO / "research" / "quiet_quitting_manifesto_2026-09-16",  # historical preservation archive
    REPO / "research" / "moreish_ontology_2026-09-13",          # author-paused / DOI-frozen
)


def _under(path: Path, trees) -> bool:
    rp = path.resolve()
    for tree in trees:
        try:
            rp.relative_to(tree)
            return True
        except ValueError:
            pass
    return False


def _excluded(path: Path) -> bool:
    return _under(path, EXCLUDE_TREES)


def main() -> int:
    files = [f for f in math_guard.all_markdown([str(REPO)]) if not _excluded(f)]
    real: list = []
    advisory = 0
    suppressed_bare = 0
    archive_advisory = 0
    for f in files:
        rel = f.resolve().relative_to(REPO).as_posix()
        is_archive = cgm.classify_tier(rel) == "ARCHIVE" or _under(f, PRESERVATION_TREES)
        issues = math_guard.Scanner(rel, strict_portable=True).scan(
            f.read_text(encoding="utf-8")
        )
        display_lines = {i.line for i in issues if i.code == "DISPLAY_DELIMITER"}
        for i in issues:
            if is_archive:
                archive_advisory += 1
            elif i.code in ADVISORY_CODES:
                advisory += 1
            elif i.code == "BARE_TEX" and i.line in display_lines:
                suppressed_bare += 1  # artifact of carve-out 3, not a real bug
            else:
                real.append(i)
    for i in real:
        print(f"{i.path}:{i.line}: {i.code}: {i.message}")
    print(
        f"check-math-portable: {len(files)} file(s); {len(real)} portable finding(s); "
        f"suppressed: {advisory} single-line-$$, {suppressed_bare} co-located BARE_TEX, "
        f"{archive_advisory} frozen/preserved; fixtures + calibration kit excluded"
    )
    return 1 if real else 0


if __name__ == "__main__":
    raise SystemExit(main())
