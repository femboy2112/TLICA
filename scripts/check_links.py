#!/usr/bin/env python3
"""Internal Markdown link checker for the TLICA archive.

Walks every ``*.md`` file in the archive and verifies that each *local* relative
link target exists on disk. Web URLs (``http``/``https``/``mailto``), pure
in-page anchors (``#section``), and absolute paths are skipped; a ``path#anchor``
link has only its file part checked (anchors are not resolved).

Exit status:
    0  no broken local links
    1  at least one broken local link (paths printed to stderr)

Pure standard library: no third-party dependencies, no network. Deliberately
conservative -- reports a link as broken only when the resolved target file
genuinely does not exist. This is the ``make links`` gate; run it after adding
or moving any document, and always when registering a new application paper.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

# [text](target)  and  ![alt](target) ; also grabs an optional (path "title").
LINK_RE = re.compile(r'!?\[[^\]]*\]\(\s*(<[^>]+>|[^)\s]+)')

SKIP_PREFIXES = ("http://", "https://", "mailto:", "tel:", "ftp://", "#", "//")


def is_local(target: str) -> bool:
    if target.startswith(SKIP_PREFIXES):
        return False
    if "://" in target:
        return False
    if target.startswith("/"):  # absolute filesystem/site path: out of scope
        return False
    return True


def file_part(target: str) -> str:
    """Strip angle brackets, a trailing ``#anchor``, and a link title."""
    t = target.strip()
    if t.startswith("<") and t.endswith(">"):
        t = t[1:-1]
    t = t.split("#", 1)[0]
    t = t.split(" ", 1)[0]  # drop any (path "title") remainder
    return t.strip()


def iter_md_files():
    for p in sorted(REPO.rglob("*.md")):
        if ".git" in p.parts:
            continue
        yield p


def main() -> int:
    broken: list[str] = []
    checked = 0
    files = 0
    for md in iter_md_files():
        files += 1
        try:
            lines = md.read_text(encoding="utf-8").splitlines()
        except UnicodeDecodeError:
            continue
        for lineno, line in enumerate(lines, 1):
            for m in LINK_RE.finditer(line):
                target = m.group(1)
                if not is_local(target):
                    continue
                fp = file_part(target)
                if not fp:  # was a pure #anchor after stripping
                    continue
                checked += 1
                resolved = (md.parent / fp).resolve()
                if not resolved.exists():
                    rel = md.relative_to(REPO)
                    broken.append(f"{rel}:{lineno}  ->  {target}  (MISSING)")

    if broken:
        print(f"BROKEN LINKS: {len(broken)} of {checked} local links unresolved",
              file=sys.stderr)
        for b in broken:
            print("  " + b, file=sys.stderr)
        return 1
    print(f"PASS check_links: all {checked} local Markdown links resolve "
          f"across {files} files")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
