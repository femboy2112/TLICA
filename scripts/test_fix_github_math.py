#!/usr/bin/env python3
"""Calibration tests for fix_github_math.py.

Every trap that would corrupt real TLICA math is a test here. A fixer that cannot
pass these is not trusted to rewrite the archive. Pure stdlib unittest.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import fix_github_math as fx  # noqa: E402


def conv(text: str) -> str:
    return fx.convert_text(text)[0]


class InlineParen(unittest.TestCase):
    def test_simple_inline(self):
        self.assertEqual(conv(r"TLICA's \(\rho\), \(\lambda\) worth."),
                         r"TLICA's $\rho$, $\lambda$ worth.")

    def test_inline_with_nested_parens_content(self):
        self.assertEqual(conv(r"the bundle \(\mathcal G=(\Pi,\mu)\) is weak"),
                         r"the bundle $\mathcal G=(\Pi,\mu)$ is weak")

    def test_two_on_one_line(self):
        self.assertEqual(conv(r"for \(c\) in \(A\) and \(d\) in \(B\),"),
                         r"for $c$ in $A$ and $d$ in $B$,")


class DisplayDelimiters(unittest.TestCase):
    def test_standalone_block(self):
        src = "text\n\\[\nx=y\n\\]\nmore"
        self.assertEqual(conv(src), "text\n$$\nx=y\n$$\nmore")

    def test_blockquoted_block(self):
        src = "> \\[\n> d=f(c),\n> \\]"
        self.assertEqual(conv(src), "> $$\n> d=f(c),\n> $$")

    def test_operatorname_inside_display(self):
        src = "\\[\n\\operatorname{cl}_\\Theta(\\omega)\n\\]"
        self.assertEqual(conv(src), "$$\n\\mathrm{cl}_\\Theta(\\omega)\n$$")


class MustNotCorrupt(unittest.TestCase):
    def test_matrix_rowbreak_survives(self):
        # \\[4pt] is a backslash-escaped row break, NOT a display opener
        src = "$$\n\\begin{array}{cc}a & b \\\\[4pt] c & d\\end{array}\n$$"
        self.assertEqual(conv(src), src)

    def test_rowbreak_inside_converted_block_survives(self):
        src = "\\[\n\\begin{array}{cc}a & b \\\\[4pt] c & d\\end{array}\n\\]"
        self.assertEqual(conv(src),
                         "$$\n\\begin{array}{cc}a & b \\\\[4pt] c & d\\end{array}\n$$")

    def test_code_span_preserved(self):
        src = r"replaced `\operatorname{...}` and `\(...\)` in the sweep"
        self.assertEqual(conv(src), src)

    def test_fenced_code_preserved(self):
        src = "```\n\\(x\\) and \\operatorname{F}\n```"
        self.assertEqual(conv(src), src)

    def test_fenced_math_gets_opname_swap_only(self):
        src = "```math\n\\operatorname{MaxFlow}(s,t)\n```"
        self.assertEqual(conv(src), "```math\n\\mathrm{MaxFlow}(s,t)\n```")

    def test_currency_untouched(self):
        src = "it cost $5 and $10 yesterday"
        self.assertEqual(conv(src), src)

    def test_existing_dollar_math_opname_only(self):
        self.assertEqual(conv(r"inline $\operatorname{cl}(x)$ here"),
                         r"inline $\mathrm{cl}(x)$ here")

    def test_existing_dollar_math_otherwise_untouched(self):
        self.assertEqual(conv(r"inline $\rho = R(G)$ here"),
                         r"inline $\rho = R(G)$ here")


class Operatorname(unittest.TestCase):
    def test_nonstar(self):
        self.assertEqual(swap(r"\operatorname{MaxFlow}"), r"\mathrm{MaxFlow}")

    def test_star_keeps_limits(self):
        self.assertEqual(swap(r"\operatorname*{arg\,max}"),
                         r"\mathop{\mathrm{arg\,max}}")


class SetextShatter(unittest.TestCase):
    def test_lone_equals_merged_up(self):
        src = "$$\nW_t\n=\n(K_t, A_t)\n$$"
        self.assertEqual(conv(src), "$$\nW_t =\n(K_t, A_t)\n$$")

    def test_lone_dash_merged_up(self):
        src = "$$\na\n-\nb\n$$"
        self.assertEqual(conv(src), "$$\na -\nb\n$$")

    def test_multi_equals_merged(self):
        src = "$$\nx\n===\ny\n$$"
        self.assertEqual(conv(src), "$$\nx ===\ny\n$$")

    def test_blockquoted_setext_merged(self):
        src = "> $$\n> W\n> =\n> v\n> $$"
        self.assertEqual(conv(src), "> $$\n> W =\n> v\n> $$")

    def test_setext_only_inside_display(self):
        # a real setext heading OUTSIDE a $$ block must be left alone
        src = "Heading\n=======\n\nbody"
        self.assertEqual(conv(src), src)

    def test_ampersand_equals_not_touched(self):
        # &= is not a pure setext underline; it must survive (alignment)
        src = "$$\n\\begin{aligned}a &= b\\\\ &= c\\end{aligned}\n$$"
        self.assertEqual(conv(src), src)

    def test_converted_bracket_block_setext_fixed(self):
        # \[ ... \] with a lone = inside -> $$ block with = merged
        src = "\\[\nW\n=\nv\n\\]"
        self.assertEqual(conv(src), "$$\nW =\nv\n$$")


class Idempotent(unittest.TestCase):
    def test_double_apply_is_noop(self):
        src = "text \\(\\rho\\)\n\\[\n\\operatorname{cl}(x)\n\\]\n`\\(code\\)`"
        once = conv(src)
        twice = conv(once)
        self.assertEqual(once, twice)

    def test_already_clean_untouched(self):
        src = "already $\\rho$ and\n$$\nx=y\n$$\nclean"
        self.assertEqual(conv(src), src)


def swap(s):
    return fx.swap_operatorname(s)


if __name__ == "__main__":
    unittest.main(verbosity=2)
