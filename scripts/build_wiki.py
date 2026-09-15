#!/usr/bin/env python3
"""
build_wiki.py -- generate the GitHub Wiki mirror from the authoritative ``docs/``.

``docs/`` is the source of truth: it is gated by ``make validate`` (link integrity,
self-containment, term pins) and versioned *atomically* with the code and papers it
documents.  The GitHub Wiki lives in a SEPARATE git repository
(``TLICA.wiki.git``) and therefore cannot see this repo's tree or run its checks --
so we never author there.  Instead the Wiki is a GENERATED MIRROR of ``docs/``, the
same way the PDFs are generated from the Markdown: edit ``docs/``, then run
``make wiki``.

Transforms (``docs/`` Markdown -> Wiki Markdown):

  * ``docs/README.md``        -> ``Home.md``          (the Wiki landing page)
  * ``docs/<slug>.md``        -> ``<slug>.md``        (flat; page name == slug)
  * internal  ``](<slug>.md[#a])``      -> ``](<slug>[#a])``    (drop ``.md``; README -> Home)
  * boundary  ``](../<dir>/<f>[#a])``   -> ``](<BLOB>/<dir>/<f>[#a])``   absolute blob URL
  * boundary  ``](../<dir>/)``          -> ``](<TREE>/<dir>/)``          absolute tree URL
  * ``http(s)://`` / ``mailto:`` / pure ``#anchor``        -> unchanged

A boundary link is any ``../`` target: it points OUT of ``docs/`` into the code repo
(``foundation/``, ``applications/``, ``research/``, root ``README.md``), which the Wiki
repo cannot resolve relatively -- so it is rewritten to an absolute github.com URL.

Also emits the Wiki's global chrome: ``_Sidebar.md`` (navigation mirrored from
``docs/README.md``'s structure) and ``_Footer.md`` (a "generated, edit docs/" notice).

Usage:  ``build_wiki.py <output-dir>``  -- wipes ``*.md`` in <output-dir> (leaving
``.git`` alone) and writes the fresh mirror.
"""
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
DOCS = REPO / "docs"

# Repo identity for absolute boundary links.
NWO = "femboy2112/TLICA"
BLOB = f"https://github.com/{NWO}/blob/main"
TREE = f"https://github.com/{NWO}/tree/main"

# Matches an inline-link / image target: the "(...)" in "](...)".
LINK_RE = re.compile(r"\]\(([^)]+)\)")


def transform_target(target: str) -> str:
    """Rewrite a single Markdown link target from docs/ space into Wiki space."""
    target = target.strip()

    # Split off a trailing "#anchor" (keep it verbatim).
    if "#" in target:
        path, anchor = target.split("#", 1)
        anchor = "#" + anchor
    else:
        path, anchor = target, ""

    # Pure same-page anchor, or an external/absolute link: leave untouched.
    if path == "":
        return target
    if re.match(r"^(https?:|mailto:|#)", path):
        return target

    # Boundary link: "../<something>" points out of docs/ into the code repo.
    if path.startswith("../"):
        rest = path
        while rest.startswith("../"):
            rest = rest[3:]
        rest = rest.lstrip("/")
        base = TREE if path.endswith("/") else BLOB
        return f"{base}/{rest}{anchor}"

    # Internal docs page: drop ".md"; README is the Wiki's Home.
    if path.endswith(".md"):
        stem = path[:-3]
        if stem == "README":
            stem = "Home"
        return f"{stem}{anchor}"

    # Anything else (defensive): pass through unchanged.
    return target


def transform_body(text: str) -> str:
    """Apply the link transform across a page body, leaving everything else byte-faithful."""
    return LINK_RE.sub(lambda m: "](" + transform_target(m.group(1)) + ")", text)


def out_name(md: Path) -> str:
    """docs/README.md -> Home.md ; docs/<slug>.md -> <slug>.md."""
    return "Home.md" if md.stem == "README" else md.name


def build_sidebar(readme_text: str) -> str:
    """Mirror docs/README.md's Part headings + top-level page links as a Wiki sidebar.

    Groups links under their ``## `` heading, and emits a heading only when it
    actually has links beneath it (so heading-only sections like the closing
    one-paragraph reminder do not leave a dangling header in the sidebar).
    """
    groups: list[tuple[str, list[str]]] = []
    header, links = None, []
    for line in readme_text.splitlines():
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            if header is not None and links:
                groups.append((header, links))
            header, links = h.group(1), []
            continue
        # A top-level list item linking to an internal flat page.
        li = re.match(r"^-\s+\[(.+?)\]\(([A-Za-z0-9][\w-]*)\.md\)", line)
        if li:
            text = li.group(1).strip().strip("*").strip()
            slug = "Home" if li.group(2) == "README" else li.group(2)
            links.append(f"- [{text}]({slug})")
    if header is not None and links:
        groups.append((header, links))

    out = ["### TLICA Wiki", "", "[Home](Home)"]
    for header, links in groups:
        out += ["", f"**{header}**", ""]
        out += links
    return "\n".join(out).strip() + "\n"


FOOTER = (
    "---\n\n"
    "*This Wiki is a generated mirror of the [`docs/`]"
    f"({TREE}/docs) directory in the main repository -- do not edit pages here; "
    "edit `docs/` and run `make wiki`. "
    f"Source of truth and full history live in [{NWO}](https://github.com/{NWO}).*\n"
)


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: build_wiki.py <output-dir>", file=sys.stderr)
        return 2
    out_dir = Path(sys.argv[1]).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    # Wipe stale generated Markdown so deletions/renames in docs/ propagate.
    for stale in out_dir.glob("*.md"):
        stale.unlink()

    pages = sorted(DOCS.glob("*.md"))
    if not pages:
        print(f"build_wiki: no pages found in {DOCS}", file=sys.stderr)
        return 1

    readme_text = ""
    written = 0
    for md in pages:
        text = md.read_text(encoding="utf-8")
        if md.stem == "README":
            readme_text = text
        (out_dir / out_name(md)).write_text(transform_body(text), encoding="utf-8")
        written += 1

    (out_dir / "_Sidebar.md").write_text(build_sidebar(readme_text), encoding="utf-8")
    (out_dir / "_Footer.md").write_text(FOOTER, encoding="utf-8")

    print(f"build_wiki: wrote {written} pages + _Sidebar.md + _Footer.md to {out_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
