#!/usr/bin/env python3
"""Finite stipulated support models, not measurements or simulations of people.

Run: python3 support_demo.py
No packages, network, repository writes, or human data are required.
"""
from __future__ import annotations

import itertools
import json
import sys
import unittest
from typing import Callable, FrozenSet

FEATURES = frozenset({"activity", "payoff", "opposition", "feasible"})
State = FrozenSet[str]
Rule = Callable[[State], bool]


def action(rule: Rule, active: State) -> bool:
    """Evaluate only complete toy states: absent names mean stipulated false."""
    unknown = active - FEATURES
    if unknown:
        raise ValueError(f"Unknown features: {sorted(unknown)}")
    return bool(rule(active))


RULES: dict[str, Rule] = {
    "activity_supported": lambda s: {"feasible", "activity"} <= s,
    "payoff_supported": lambda s: {"feasible", "payoff"} <= s,
    "opposition_supported": lambda s: {"feasible", "opposition"} <= s,
    "redundant_support": lambda s: "feasible" in s and bool({"activity", "payoff"} & s),
    "conjunctive_support": lambda s: {"feasible", "activity", "payoff"} <= s,
}


def subsets(names: State):
    ordered = sorted(names)
    for count in range(len(ordered) + 1):
        for values in itertools.combinations(ordered, count):
            yield frozenset(values)


def minimal_supports(rule: Rule) -> list[list[str]]:
    """Inclusion-minimal sufficient sets for this finite, complete model."""
    found: list[State] = []
    for state in subsets(FEATURES):
        if action(rule, state) and not any(old <= state for old in found):
            found.append(state)
    return [sorted(state) for state in found]


class SupportTests(unittest.TestCase):
    def test_01_same_baseline_does_not_identify_rule(self):
        self.assertTrue(all(action(rule, FEATURES) for rule in RULES.values()))

    def test_02_payoff_withdrawal_separates_rules(self):
        state = FEATURES - {"payoff"}
        self.assertTrue(action(RULES["activity_supported"], state))
        self.assertFalse(action(RULES["payoff_supported"], state))

    def test_03_opposition_withdrawal_separates_rules(self):
        state = FEATURES - {"opposition"}
        self.assertTrue(action(RULES["activity_supported"], state))
        self.assertFalse(action(RULES["opposition_supported"], state))

    def test_04_feasibility_is_a_separate_gate(self):
        state = FEATURES - {"feasible"}
        self.assertFalse(any(action(rule, state) for rule in RULES.values()))

    def test_05_redundancy_masks_single_withdrawals(self):
        rule = RULES["redundant_support"]
        self.assertTrue(action(rule, FEATURES - {"activity"}))
        self.assertTrue(action(rule, FEATURES - {"payoff"}))
        self.assertFalse(action(rule, FEATURES - {"activity", "payoff"}))

    def test_06_conjunction_is_not_an_alternative_path(self):
        rule = RULES["conjunctive_support"]
        self.assertFalse(action(rule, FEATURES - {"activity"}))
        self.assertFalse(action(rule, FEATURES - {"payoff"}))

    def test_07_minimal_supports_match_explicit_sets(self):
        self.assertEqual(minimal_supports(RULES["activity_supported"]),
                         [["activity", "feasible"]])
        self.assertEqual(minimal_supports(RULES["redundant_support"]),
                         [["activity", "feasible"], ["feasible", "payoff"]])
        self.assertEqual(minimal_supports(RULES["conjunctive_support"]),
                         [["activity", "feasible", "payoff"]])

    def test_08_irrelevant_feature_is_null_control(self):
        rule = RULES["activity_supported"]
        self.assertEqual(action(rule, FEATURES),
                         action(rule, FEATURES - {"opposition"}))

    def test_09_unknown_feature_fails_loudly(self):
        with self.assertRaises(ValueError):
            action(RULES["activity_supported"], FEATURES | {"authenticity"})

    def test_10_no_support_remains_false(self):
        self.assertFalse(any(action(rule, frozenset()) for rule in RULES.values()))

    def test_11_contrarianism_still_depends_on_signal(self):
        compliance = lambda signal: signal
        opposition = lambda signal: 1 - signal
        self.assertNotEqual(compliance(0), compliance(1))
        self.assertNotEqual(opposition(0), opposition(1))

    def test_12_mutated_feasibility_rule_is_detected(self):
        mutant = lambda state: "activity" in state
        state = FEATURES - {"feasible"}
        self.assertNotEqual(action(mutant, state),
                            action(RULES["activity_supported"], state))

    def test_13_mutated_conjunction_is_detected(self):
        mutant = RULES["redundant_support"]
        state = FEATURES - {"payoff"}
        self.assertNotEqual(action(mutant, state),
                            action(RULES["conjunctive_support"], state))


def main() -> int:
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(SupportTests)
    result = unittest.TextTestRunner(stream=sys.stderr, verbosity=2).run(suite)
    interventions = {
        "baseline": FEATURES,
        "without_payoff": FEATURES - {"payoff"},
        "without_opposition": FEATURES - {"opposition"},
        "without_activity": FEATURES - {"activity"},
        "without_activity_and_payoff": FEATURES - {"activity", "payoff"},
        "without_feasibility": FEATURES - {"feasible"},
    }
    print(json.dumps({
        "scope": "stipulated Boolean models; no empirical or clinical inference",
        "tests_run": result.testsRun,
        "failures": len(result.failures),
        "errors": len(result.errors),
        "all_passed": result.wasSuccessful(),
        "predictions": {
            name: {key: action(rule, state) for key, state in interventions.items()}
            for name, rule in RULES.items()
        },
        "minimal_supports": {name: minimal_supports(rule) for name, rule in RULES.items()},
    }, indent=2, sort_keys=True))
    return 0 if result.wasSuccessful() else 1


if __name__ == "__main__":
    raise SystemExit(main())
