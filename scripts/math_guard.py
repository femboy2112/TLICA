#!/usr/bin/env python3
"""SMPTeX: conservative, stdlib-only GitHub Markdown math preflight.

This is a source-level guard, NOT a MathJax parser or a browser-render guarantee.
"""
from __future__ import annotations

import argparse
from dataclasses import asdict, dataclass
import json
import os
from pathlib import Path
import re
import sys
from typing import Iterable

FENCE = re.compile(r"^ {0,3}(`{3,}|~{3,})([^\n]*)$")
ISOLATED_DISPLAY = re.compile(r"^\s*\$\$\s*$")
ENV_TOKEN = re.compile(r"\\(begin|end)\{([A-Za-z][A-Za-z0-9*]*)\}")
PROSE_TEX = re.compile(r"(?<!\\)\\(?:frac|sqrt|sum|prod|int|mathbb|mathcal|begin|operatorname|lim|left|right)\b")
BAD_DELIMITER = re.compile(r"(?<!\\)\\[\[(]")
UNSAFE = (
    "newcommand", "renewcommand", "providecommand", "usepackage",
    "includegraphics", "input", "require", "def",
)
SKIP_DIRS = {".git", ".venv", "venv", "node_modules", ".tox", ".mypy_cache", ".pytest_cache", "dist", "build"}


@dataclass(frozen=True)
class Issue:
    path: str
    line: int
    code: str
    message: str


class Scanner:
    def __init__(self, path: str, strict_portable: bool = False):
        self.path = path
        self.strict_portable = strict_portable
        self.issues: list[Issue] = []

    def error(self, line: int, code: str, message: str) -> None:
        self.issues.append(Issue(self.path, line, code, message))

    @staticmethod
    def escaped(s: str, pos: int) -> bool:
        k = pos - 1
        while k >= 0 and s[k] == "\\":
            k -= 1
        return ((pos - k - 1) % 2) == 1

    def math(self, tex: str, line: int, in_table: bool = False) -> None:
        if not tex.strip():
            self.error(line, "EMPTY_MATH", "Empty math expression")
            return
        if in_table and "|" in tex:
            self.error(line, "TABLE_PIPE", "Raw pipe inside table math may split Markdown cells; use \\mid, \\lvert/\\rvert, or move the equation outside the table")
        # Brace check, ignoring escaped literal braces (not TeX control groups).
        stack: list[int] = []
        i = 0
        while i < len(tex):
            ch = tex[i]
            if ch == "\\" and i + 1 < len(tex):
                if tex[i + 1] in "{}":
                    i += 2
                    continue
                i += 1
                continue
            if ch == "{":
                stack.append(i)
            elif ch == "}":
                if stack:
                    stack.pop()
                else:
                    self.error(line, "BRACES", "Unexpected closing brace in math")
            i += 1
        if stack:
            self.error(line, "BRACES", f"Unclosed opening brace(s): {len(stack)}")

        env_stack: list[str] = []
        for token in ENV_TOKEN.finditer(tex):
            action, name = token.groups()
            if action == "begin":
                env_stack.append(name)
            elif not env_stack or env_stack[-1] != name:
                self.error(line, "ENVIRONMENT", f"Unmatched end of {name!r} environment")
            else:
                env_stack.pop()
        if env_stack:
            self.error(line, "ENVIRONMENT", f"Unclosed environment(s): {', '.join(env_stack)}")

        left = len(re.findall(r"\\left(?=[\s\\().|\[\]{}<>])", tex))
        right = len(re.findall(r"\\right(?=[\s\\().|\[\]{}<>])", tex))
        if left != right:
            self.error(line, "LEFT_RIGHT", f"Unbalanced TeX delimiters: {left} left / {right} right")

        for macro in UNSAFE:
            if re.search(r"\\" + re.escape(macro) + r"(?![A-Za-z])", tex):
                self.error(line, "UNSAFE_MACRO", f"\\{macro} is outside the portable authoring policy")
        if re.search(r"\\begin\{(?:tikzcd|diagram|picture)\}", tex):
            self.error(line, "UNSAFE_ENVIRONMENT", "Graphics/diagram LaTeX environments are not in the portable profile")
        if self.strict_portable and re.search(r"\\operatorname(?:\*|\b)", tex):
            self.error(line, "UNCERTIFIED_MACRO", "Use \\mathrm{...} instead of \\operatorname{...} (explicitly rejected on the observed GitHub repository-Markdown surface; other surfaces unverified)")

    @staticmethod
    def _blank(text: str, start: int, end: int) -> str:
        return text[:start] + " " * (end - start) + text[end:]

    def inline(self, line: str, number: int) -> None:
        # Official GitHub example wraps a literal currency dollar in a span.
        s = re.sub(r"<span>\$</span>", lambda m: " " * len(m.group(0)), line)
        prose = s
        i = 0
        while i < len(s):
            if s[i] == "`":
                n = len(s[i:]) - len(s[i:].lstrip("`"))
                marker = "`" * n
                end = s.find(marker, i + n)
                if end >= 0:
                    prose = self._blank(prose, i, end + n)
                    i = end + n
                    continue
                i += n
                continue
            if s[i] != "$" or self.escaped(s, i):
                i += 1
                continue
            if s.startswith("$$", i):
                self.error(number, "DISPLAY_DELIMITER", "Use $$ alone on its own lines for portable block math")
                prose = self._blank(prose, i, i + 2)
                i += 2
                continue
            if s.startswith("$`", i):
                end = s.find("`$", i + 2)
                if end < 0:
                    self.error(number, "UNTERMINATED_INLINE", "Missing closing backtick-dollar for $`...`$ math")
                    prose = self._blank(prose, i, len(s))
                    break
                self.math(s[i + 2:end], number, in_table=s.lstrip().startswith("|"))
                prose = self._blank(prose, i, end + 2)
                i = end + 2
                continue
            j = i + 1
            while j < len(s):
                if s[j] == "$" and not self.escaped(s, j):
                    break
                j += 1
            if j >= len(s):
                self.error(number, "UNTERMINATED_INLINE", "Unpaired $; for currency use an escaped dollar or GitHub's <span>$</span> form")
                prose = self._blank(prose, i, len(s))
                break
            self.math(s[i + 1:j], number, in_table=s.lstrip().startswith("|"))
            prose = self._blank(prose, i, j + 1)
            i = j + 1
        if BAD_DELIMITER.search(prose):
            self.error(number, "ALT_DELIMITER", "Use documented GitHub math delimiters ($...$, $`...`$, $$...$$, or ```math)")
        if PROSE_TEX.search(prose):
            self.error(number, "BARE_TEX", "TeX macro in prose outside math delimiters; wrap in inline code for literal examples")

    def scan(self, content: str) -> list[Issue]:
        fence_char = ""
        fence_len = 0
        is_math_fence = False
        math_lines: list[str] = []
        math_start = 0
        display = False
        display_lines: list[str] = []
        display_start = 0
        for number, line in enumerate(content.splitlines(), 1):
            fence = FENCE.match(line)
            if fence_char:
                if (fence and fence.group(1)[0] == fence_char
                        and len(fence.group(1)) >= fence_len
                        and not fence.group(2).strip()):
                    if is_math_fence:
                        self.math("\n".join(math_lines), math_start)
                    fence_char = ""
                    is_math_fence = False
                    math_lines = []
                elif is_math_fence:
                    math_lines.append(line)
                continue
            if display:
                if ISOLATED_DISPLAY.match(line):
                    self.math("\n".join(display_lines), display_start)
                    display = False
                    display_lines = []
                else:
                    display_lines.append(line)
                continue
            if fence:
                fence_char = fence.group(1)[0]
                fence_len = len(fence.group(1))
                language = fence.group(2).strip().split(maxsplit=1)[0].lower() if fence.group(2).strip() else ""
                is_math_fence = language == "math"
                if is_math_fence:
                    math_start = number
                    math_lines = []
                continue
            if ISOLATED_DISPLAY.match(line):
                display = True
                display_start = number
                display_lines = []
                continue
            self.inline(line, number)
        eof = len(content.splitlines()) or 1
        if display:
            self.error(display_start, "UNTERMINATED_DISPLAY", "Missing closing $$ on its own line")
        if fence_char:
            self.error(math_start if is_math_fence else eof, "UNTERMINATED_FENCE", "Unclosed Markdown code fence")
        return self.issues


def all_markdown(paths: Iterable[str]) -> list[Path]:
    results: set[Path] = set()
    for raw in paths:
        p = Path(raw)
        if not p.exists():
            raise FileNotFoundError(str(p))
        if p.is_file():
            results.add(p)
        else:
            for root, dirs, filenames in os.walk(p):
                dirs[:] = [x for x in dirs if x not in SKIP_DIRS]
                for filename in filenames:
                    file = Path(root) / filename
                    if file.suffix.lower() in {".md", ".markdown", ".mdown"}:
                        results.add(file)
    return sorted(results)


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("paths", nargs="*", default=["."], help="Markdown files or directories to scan")
    p.add_argument("--strict-portable", action="store_true", help="Disallow uncertified macros such as operatorname")
    p.add_argument("--json", action="store_true", help="Emit machine-readable findings")
    p.add_argument("--exclude", action="append", default=[], metavar="PATH", help="Exclude an exact repository-relative Markdown path (must be checked separately)")
    args = p.parse_args(argv)
    try:
        paths = all_markdown(args.paths)
    except (FileNotFoundError, PermissionError) as exc:
        print(f"math_guard: path error: {exc}", file=sys.stderr)
        return 2
    excluded = {Path(value).as_posix().removeprefix("./") for value in args.exclude}
    results: list[Issue] = []
    scanned = 0
    for path in paths:
        try:
            relative = path.resolve().relative_to(Path.cwd().resolve()).as_posix()
        except ValueError:
            relative = path.as_posix()
        if relative in excluded:
            continue
        scanned += 1
        try:
            content = path.read_text(encoding="utf-8")
        except (UnicodeError, OSError) as exc:
            results.append(Issue(str(path), 1, "READ_ERROR", str(exc)))
            continue
        results.extend(Scanner(str(path), args.strict_portable).scan(content))
    if args.json:
        print(json.dumps({"scanned": scanned, "issues": [asdict(x) for x in results]}, indent=2))
    else:
        for issue in results:
            print(f"{issue.path}:{issue.line}: {issue.code}: {issue.message}")
        print(f"SMPTeX: {scanned} Markdown file(s) scanned; {len(results)} issue(s)")
    return 1 if results else 0


if __name__ == "__main__":
    raise SystemExit(main())
