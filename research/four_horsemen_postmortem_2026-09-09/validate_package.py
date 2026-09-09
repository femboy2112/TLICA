#!/usr/bin/env python3
"""Scoped document checks and explicit toy arithmetic; no empirical validation."""
from __future__ import annotations

import hashlib
import json
import re
import sys
import tempfile
from fractions import Fraction
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parent
SOURCE = re.compile(r"\[((?:CTX|P|H|D|W|S|E|B)-\d{2})\]")
INLINE = re.compile(r"\[[^\]\n]*\]\(([^)\n]+)\)")
REFERENCE = re.compile(r"^\[[^\]\n]+\]:\s*(\S+)", re.MULTILINE)


def anchors(text: str) -> set[str]:
    """Subset of GitHub heading slugs sufficient for this package's ASCII IDs."""
    found: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"^#{1,6}\s+(.+?)\s*#*\s*$", line)
        if match:
            slug = re.sub(r"[^\w\- ]", "", match.group(1).lower()).replace(" ", "-")
            found.add(slug)
    return found


def link_errors(path: Path, text: str, root: Path) -> list[str]:
    errors: list[str] = []
    targets = INLINE.findall(text) + REFERENCE.findall(text)
    for target in targets:
        parsed = urlsplit(target)
        if parsed.scheme or parsed.netloc:
            continue  # Network availability is deliberately not tested.
        resolved = (path.parent / unquote(parsed.path)).resolve() if parsed.path else path
        if not resolved.is_relative_to(root.resolve()):
            errors.append(f"outside package: {target}")
        elif not resolved.is_file():
            errors.append(f"missing target: {target}")
        elif parsed.fragment and resolved.suffix == ".md":
            if unquote(parsed.fragment) not in anchors(resolved.read_text(encoding="utf-8")):
                errors.append(f"missing anchor: {target}")
    return errors


def require(condition: bool, message: str) -> None:
    if not condition:
        raise ValueError(message)


def main() -> int:
    documents = sorted(ROOT.glob("*.md"))
    require(len(documents) == 5, "Expected exactly five authored Markdown documents")
    ledger = (ROOT / "SOURCES_AND_CLAIM_LEDGER.md").read_text(encoding="utf-8")
    defined = set(re.findall(r"^## ((?:CTX|P|H|D|W|S|E|B)-\d{2})$", ledger, re.MULTILINE))
    problems: list[str] = []
    for path in documents:
        text = path.read_text(encoding="utf-8")
        problems += [f"{path.name}: {error}" for error in link_errors(path, text, ROOT)]
        unknown = set(SOURCE.findall(text)) - defined
        if unknown:
            problems.append(f"{path.name}: undefined source IDs {sorted(unknown)}")
        if "\ue200" in text or "?token=" in text or "github_pat_" in text:
            problems.append(f"{path.name}: transient citation or credential marker")
        if not text.endswith("\n"):
            problems.append(f"{path.name}: missing final newline")
    require(not problems, "\n".join(problems))

    with tempfile.TemporaryDirectory() as directory:
        root = Path(directory)
        a, b = root / "a.md", root / "b.md"
        a.write_text("# A\n", encoding="utf-8")
        b.write_text("# Good anchor\n", encoding="utf-8")
        require(not link_errors(a, "[ok](b.md#good-anchor)", root), "positive link control failed")
        require(bool(link_errors(a, "[bad](absent.md)", root)), "missing-file mutation escaped")
        require(bool(link_errors(a, "[bad](b.md#absent)", root)), "anchor mutation escaped")
        require(bool(link_errors(a, "[bad](../outside.md)", root)), "escape mutation escaped")

    population = set(range(10000))
    group = set(range(100))
    harmful = set(range(10))
    rate = Fraction(len(harmful), len(population))
    group_rate = Fraction(len(group), len(population))
    group_given_harm = Fraction(len(group & harmful), len(harmful))
    harm_given_group = Fraction(len(group & harmful), len(group))
    require(harm_given_group == group_given_harm * rate / group_rate, "Bayes identity failed")

    flags = {
        "informative_A": group,
        "misleading_B": set(range(100, 200)),
        "uninformative_control": population,
    }
    worlds: dict[str, dict[str, int | str]] = {}
    for name, flagged in flags.items():
        true_positive = len(flagged & harmful)
        false_positive = len(flagged - harmful)
        worlds[name] = {
            "flagged": len(flagged),
            "true_positive": true_positive,
            "false_positive": false_positive,
            "precision": str(Fraction(true_positive, len(flagged))),
            "invented_utility": 20 * true_positive - len(flagged),
        }
    require(worlds["informative_A"]["invented_utility"] == 100, "positive world mismatch")
    require(worlds["misleading_B"]["invented_utility"] == -100, "negative world mismatch")
    # A constant flag has precision exactly equal to the population prevalence.
    null_precision = Fraction(len(population & harmful), len(population))
    require(null_precision == rate, "null-control precision must equal prevalence")
    require(worlds["uninformative_control"]["precision"] == str(rate), "uninformative flag mismatch")

    blobs = {}
    for path in sorted(ROOT.iterdir()):
        if path.is_file() and path.name != "validation_output.txt":
            data = path.read_bytes()
            blobs[path.name] = hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
    print(json.dumps({
        "status": "PASS",
        "scope": "package structure and finite constructed arithmetic only",
        "markdown_documents": len(documents),
        "registered_source_ids": len(defined),
        "link_controls": {"valid": "PASS", "missing_file_mutation": "CAUGHT", "anchor_mutation": "CAUGHT", "path_escape_mutation": "CAUGHT"},
        "fixed_group_given_harm": str(group_given_harm),
        "fixed_harm_given_group": str(harm_given_group),
        "constructed_worlds": worlds,
        "exact_uninformative_control_precision": str(null_precision),
        "full_repository_make_validate": "NOT RUN: no full checkout",
        "psychological_or_security_experiments": "NOT RUN",
        "git_blob_sha1_excluding_this_output": blobs,
    }, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (ValueError, OSError) as error:
        print(f"FAIL: {error}", file=sys.stderr)
        raise SystemExit(1)
