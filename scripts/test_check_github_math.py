#!/usr/bin/env python3
"""Calibration tests for scripts/check_github_math.py.

Positive, negative, and mutation controls (scripts/github_math_fixtures/). A checker that
cannot pass these is not trusted to scan the archive. Pure stdlib unittest.
"""
from __future__ import annotations

import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import check_github_math as chk  # noqa: E402

FIX = HERE / "github_math_fixtures"


def rules(fixture: str, tier: str):
    text = (FIX / fixture).read_text(encoding="utf-8")
    return chk.scan_file(f"scripts/github_math_fixtures/{fixture}", text, tier)


def ruleset(fixture, tier):
    return {f.rule for f in rules(fixture, tier)}


def sev_of(fixture, tier, rule):
    return {f.sev for f in rules(fixture, tier) if f.rule == rule}


class PositiveControls(unittest.TestCase):
    def test_positive_is_clean_at_front(self):
        found = rules("positive.md", "FRONT")
        self.assertEqual(found, [], f"positive control produced findings: "
                                    f"{[(f.rule, f.line) for f in found]}")

    def test_source_in_code_is_not_math(self):
        found = rules("negative_code_is_source.md", "FRONT")
        self.assertEqual(found, [], f"code/source wrongly flagged: "
                                    f"{[(f.rule, f.line) for f in found]}")

    def test_currency_does_not_false_positive(self):
        found = rules("negative_currency.md", "FRONT")
        self.assertEqual(found, [], f"currency wrongly flagged: "
                                    f"{[(f.rule, f.line) for f in found]}")


class NegativeControls(unittest.TestCase):
    def test_operatorname_flagged_and_is_error_on_front(self):
        self.assertIn("GH-OPERATORNAME", ruleset("negative_operatorname.md", "FRONT"))
        self.assertEqual(sev_of("negative_operatorname.md", "FRONT", "GH-OPERATORNAME"), {2})

    def test_legacy_delim_flagged_and_is_error_on_front(self):
        self.assertIn("GH-LEGACY-DELIM", ruleset("negative_legacy_delim.md", "FRONT"))
        self.assertEqual(sev_of("negative_legacy_delim.md", "FRONT", "GH-LEGACY-DELIM"), {2})

    def test_unclosed_display_flagged(self):
        self.assertIn("GH-UNCLOSED-DISPLAY", ruleset("negative_unclosed_display.md", "FRONT"))

    def test_setext_shatter_flagged_as_error_on_front(self):
        self.assertIn("GH-SETEXT-SHATTER", ruleset("negative_setext_shatter.md", "FRONT"))
        self.assertEqual(sev_of("negative_setext_shatter.md", "FRONT", "GH-SETEXT-SHATTER"), {2})

    def test_setext_shatter_does_not_flag_aligned_ampersand(self):
        # the &= alignment block must not trip the setext rule
        found = [f for f in rules("negative_setext_shatter.md", "FRONT")
                 if f.rule == "GH-SETEXT-SHATTER"]
        # exactly one shatter finding (the lone '='), not the &= lines
        self.assertEqual(len(found), 1, f"expected 1 setext finding, got "
                                        f"{[(f.rule, f.line) for f in found]}")


class MutationControls(unittest.TestCase):
    def test_unclosed_inline_dollar_flagged(self):
        self.assertIn("GH-INLINE-DOLLAR", ruleset("mutation_unclosed_inline.md", "FRONT"))

    def test_brace_imbalance_flagged(self):
        self.assertIn("GH-BRACE-IMBALANCE", ruleset("mutation_brace.md", "FRONT"))


class TierDowngrades(unittest.TestCase):
    def test_legacy_delim_warns_on_research(self):
        self.assertEqual(sev_of("negative_legacy_delim.md", "RESEARCH", "GH-LEGACY-DELIM"), {1})

    def test_legacy_delim_info_on_archive(self):
        self.assertEqual(sev_of("negative_legacy_delim.md", "ARCHIVE", "GH-LEGACY-DELIM"), {0})

    def test_operatorname_warns_on_research(self):
        # research dossiers are preserved manuscripts: reported, but not a gate failure
        self.assertEqual(sev_of("negative_operatorname.md", "RESEARCH", "GH-OPERATORNAME"), {1})

    def test_operatorname_info_on_archive(self):
        # still reported, but never fails the gate for byte-frozen material
        self.assertEqual(sev_of("negative_operatorname.md", "ARCHIVE", "GH-OPERATORNAME"), {0})

    def test_tier_classification(self):
        self.assertEqual(chk.classify_tier("README.md"), "FRONT")
        self.assertEqual(chk.classify_tier("docs/glossary.md"), "FRONT")
        self.assertEqual(chk.classify_tier("research/foo_2026/README.md"), "RESEARCH")
        self.assertEqual(chk.classify_tier("foundation/previous_v5.3.3/1.md"), "ARCHIVE")
        self.assertEqual(chk.classify_tier("research/x/originals/y.md"), "ARCHIVE")


if __name__ == "__main__":
    unittest.main(verbosity=2)
