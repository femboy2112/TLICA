"""Mutation controls: known-valid documents pass; deliberately broken ones fail."""
import importlib.util
from pathlib import Path
import tempfile
import os
import io
from contextlib import redirect_stdout
import unittest

MODULE = Path(__file__).resolve().parents[1] / "scripts" / "math_guard.py"
spec = importlib.util.spec_from_file_location("math_guard", MODULE)
import sys
math_guard = importlib.util.module_from_spec(spec)
sys.modules[spec.name] = math_guard
spec.loader.exec_module(math_guard)


def errors(src: str, strict: bool = True):
    return math_guard.Scanner("fixture.md", strict).scan(src)


class MathGuardTests(unittest.TestCase):
    def test_exclude_specific_probe(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "ordinary.md").write_text(r"$\operatorname{rank}(A)$", encoding="utf8")
            (root / "probe.md").write_text(r"$\operatorname{rank}(A)$", encoding="utf8")
            orig = Path.cwd()
            os.chdir(root)
            try:
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(math_guard.main([".", "--strict-portable", "--exclude", "probe.md"]), 1)
                    self.assertEqual(math_guard.main(["probe.md"]), 0)
            finally:
                os.chdir(orig)

    def test_exclude_exact_not_prefix(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "probe.md").write_text(r"$\operatorname{rank}(A)$", encoding="utf8")
            orig = Path.cwd()
            os.chdir(root)
            try:
                with redirect_stdout(io.StringIO()):
                    self.assertEqual(math_guard.main([".", "--strict-portable", "--exclude", "probe.md.extra"]), 1)
                    self.assertEqual(math_guard.main([".", "--strict-portable", "--exclude", "probe.md"]), 0)
            finally:
                os.chdir(orig)

    def test_svg_banner(self):
        import xml.etree.ElementTree as ET
        root = ET.parse(Path(__file__).resolve().parents[1] / "assets" / "smptex-test-pattern.svg").getroot()
        ns = {"svg":"http://www.w3.org/2000/svg"}
        bars = [r for r in root.findall("svg:rect", ns) if r.attrib.get("height") == "77"]
        self.assertEqual(len(bars), 7)
        strings = [node.text for node in root.findall("svg:text", ns)]
        self.assertIn("PLEASE STAND BY — MATHJAX FAILURE", strings)

    def test_valid_inline(self):
        self.assertEqual(errors("A $x^2+y^2=z^2$ works."), [])

    def test_valid_inline_backtick(self):
        self.assertEqual(errors("Safe with punctuation: $`a_b + x^{2}`$."), [])

    def test_valid_display(self):
        self.assertEqual(errors("Before\n\n$$\n\\frac{a}{b}=c\n$$\n\nAfter"), [])

    def test_valid_fenced_math(self):
        self.assertEqual(errors("```math\n\\begin{aligned}\na&=b\\\\\nc&=d\n\\end{aligned}\n```"), [])

    def test_literal_code_is_not_parsed(self):
        self.assertEqual(errors("Text `\\operatorname{Tr}` and `$broken`.\n\n```text\n$broken\n```"), [])

    def test_official_currency_span(self):
        self.assertEqual(errors("The price is <span>$</span>100 and $100/2=50$."), [])

    def test_escaped_currency(self):
        self.assertEqual(errors(r"Price \\$100? No, see $x=1$.".replace(r"\\$", r"\$")), [])

    def test_markdown_table_safe_math(self):
        self.assertEqual(errors("| Variable | Math |\n| --- | --- |\n| A | $a\\mid b$ |"), [])

    def test_markdown_table_raw_pipe_detected(self):
        self.assertTrue(any(e.code == "TABLE_PIPE" for e in errors("| A | $|x|$ |")))

    def test_bad_inline(self):
        self.assertTrue(any(e.code == "UNTERMINATED_INLINE" for e in errors("An equation $a+b.")))

    def test_bad_display(self):
        self.assertTrue(any(e.code == "UNTERMINATED_DISPLAY" for e in errors("$$\nx+y")))

    def test_bad_braces(self):
        self.assertTrue(any(e.code == "BRACES" for e in errors(r"$\frac{1}{x$")))

    def test_bad_environment(self):
        self.assertTrue(any(e.code == "ENVIRONMENT" for e in errors("```math\n\\begin{aligned} a &= b\n```")))

    def test_bad_left_right(self):
        self.assertTrue(any(e.code == "LEFT_RIGHT" for e in errors(r"$\left( a+b$")))

    def test_bare_tex(self):
        self.assertTrue(any(e.code == "BARE_TEX" for e in errors(r"Oops: \frac{1}{2}")))

    def test_alt_delimiter(self):
        self.assertTrue(any(e.code == "ALT_DELIMITER" for e in errors(r"Oops: \(x+1\)")))

    def test_strict_operatorname(self):
        self.assertTrue(any(e.code == "UNCERTIFIED_MACRO" for e in errors(r"$\operatorname{rank}(A)$")))
        self.assertEqual(errors(r"$\operatorname{rank}(A)$", strict=False), [])

    def test_observed_operator_ab_contexts(self):
        # Regression coverage for the three observed GitHub Markdown contexts.
        contexts = (
            ("inline", r"$\mathrm{rank}(A)=2$", r"$\operatorname{rank}(A)=2$"),
            ("display", "$$\n\\mathrm{rank}(A)=2\n$$", "$$\n\\operatorname{rank}(A)=2\n$$"),
            ("math fence", "```math\n\\mathrm{rank}(A)=2\n```", "```math\n\\operatorname{rank}(A)=2\n```"),
        )
        for name, control, challenge in contexts:
            with self.subTest(context=name):
                self.assertEqual(errors(control), [])
                self.assertEqual(errors(challenge, strict=False), [])
                self.assertTrue(any(e.code == "UNCERTIFIED_MACRO" for e in errors(challenge)))

    def test_portable_operator(self):
        self.assertEqual(errors(r"$\mathrm{rank}(A)$"), [])

    def test_nopreamble(self):
        self.assertTrue(any(e.code == "UNSAFE_MACRO" for e in errors(r"$\newcommand{\foo}{x}$")))

    def test_isolated_display_policy(self):
        self.assertTrue(any(e.code == "DISPLAY_DELIMITER" for e in errors("Text $$x$$")))

    def test_fence_missing(self):
        self.assertTrue(any(e.code == "UNTERMINATED_FENCE" for e in errors("```math\nx=y")))

    def test_unclosed_noncoding_fence(self):
        self.assertTrue(any(e.code == "UNTERMINATED_FENCE" for e in errors("```python\nprint('x')")))

    def test_control_broken_mutation(self):
        good = "$$\n\\sum_{n=1}^{N} n = N(N+1)/2\n$$"
        bad = good.replace("_{n=1}", "_{n=1")
        self.assertEqual(errors(good), [])
        self.assertTrue(errors(bad))


if __name__ == "__main__":
    unittest.main()
