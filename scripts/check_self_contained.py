#!/usr/bin/env python3
"""Self-containment invariant checker for the TLICA archive.

TLICA is the *canonical* source: its terminology must be coherent within itself
and must not depend on anything outside the tree. In particular the archive must
never link to itself by absolute GitHub URL -- an in-archive reference belongs in
a *relative* path, and an absolute ``github.com/.../TLICA/blob/<branch>/...`` link
silently pins a reader to one branch (often an unmerged ``agent/*`` draft) and
rots the moment that branch moves or merges. That exact defect shipped once and
was fixed by hand; this gate keeps it from recurring.

Each rule is a precise regular expression plus a human-readable reason. The
denylist is deliberately narrow -- only patterns that do not false-positive on
ordinary prose (so no fuzzy word like "lean", which appears innocently in "a
layer may lean on earlier layers"). Extend ``FORBIDDEN`` when a new
outside-the-tree dependency needs banning.

Exit status:
    0  archive is self-contained (no forbidden references)
    1  at least one forbidden reference (file:line printed to stderr)

Pure standard library: no third-party dependencies, no network.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# (compiled pattern, short reason). Keep every pattern specific enough that it
# cannot match ordinary prose -- a false positive here is worse than a miss,
# because it trains readers to ignore the gate.
FORBIDDEN: list[tuple[re.Pattern[str], str]] = [
    (
        re.compile(r'https?://github\.com/[^/\s)]+/TLICA/(?:blob|tree|raw)/[^)\s]+'),
        "absolute self-repo GitHub URL -- use an in-archive relative path "
        "(pins the reader to one branch and rots on merge)",
    ),
]


def iter_md_files():
    for p in sorted(REPO.rglob("*.md")):
        if ".git" in p.parts:
            continue
        yield p


def main() -> int:
    hits: list[str] = []
    files = 0
    for md in iter_md_files():
        files += 1
        try:
            lines = md.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(lines, 1):
            for pattern, reason in FORBIDDEN:
                for m in pattern.finditer(line):
                    rel = md.relative_to(REPO)
                    hits.append(f"{rel}:{lineno}  {m.group(0)}\n      -> {reason}")

    if hits:
        print(f"NOT SELF-CONTAINED: {len(hits)} forbidden reference(s) found",
              file=sys.stderr)
        for h in hits:
            print("  " + h, file=sys.stderr)
        return 1
    print(f"PASS check_self_contained: no forbidden external/self-URL "
          f"references across {files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
