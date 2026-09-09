#!/usr/bin/env python3
"""Finite countermodels for the TLICA conversation papers.

Standard library only. No human data, fitted parameters, or psychological claims.
These checks demonstrate limitations of inference in stipulated finite systems.
"""
from __future__ import annotations

from dataclasses import dataclass
from itertools import product
import json
from pathlib import Path
import sys
import unittest
from typing import Callable, Mapping

BinaryModel = Callable[[int, int], int]
CORNERS = frozenset(product((0, 1), repeat=2))


def bit(value: int) -> int:
    if type(value) is not int or value not in (0, 1):
        raise ValueError('Expected an integer binary value, not a boolean.')
    return value


def actor_only(actor: int, context: int) -> int:
    bit(context)
    return bit(actor)


def actor_context(actor: int, context: int) -> int:
    return bit(actor) ^ bit(context)


def table(model: BinaryModel) -> dict[tuple[int, int], int]:
    return {corner: bit(model(*corner)) for corner in sorted(CORNERS)}


def mixed_contrast(cells: Mapping[tuple[int, int], int]) -> int:
    if set(cells) != CORNERS:
        raise ValueError('Every cell, and only those cells, is required.')
    return cells[1, 1] - cells[1, 0] - cells[0, 1] + cells[0, 0]


def survivors(observations: Mapping[tuple[int, int], int]) -> list[str]:
    models: dict[str, BinaryModel] = {
        'actor_only': actor_only,
        'actor_context': actor_context,
    }
    return [name for name, model in models.items()
            if all(model(*corner) == observed
                   for corner, observed in observations.items())]


@dataclass(frozen=True)
class Record:
    record_id: str
    event_family: str
    kind: str


def event_family_count(records: list[Record]) -> int:
    """Bookkeeping for common event provenance, NOT a truth score."""
    return len({record.event_family for record in records})


def report() -> dict:
    base = {(0, 0): 0, (1, 0): 1}
    holdout = {(0, 1): 1, (1, 1): 0}
    archive = [Record('cut-A', 'same-encounter', 'edited'),
               Record('cut-B', 'same-encounter', 'edited'),
               Record('reaction', 'same-encounter', 'derivative')]
    return {
        'scope': 'Stipulated finite systems only; no observations about people.',
        'baseline_survivors': survivors(base),
        'fresh_holdout_survivors': survivors(base | holdout),
        'actor_context_table': [dict(actor=a, context=n, output=v)
                                for (a, n), v in table(actor_context).items()],
        'full_factorial_mixed_contrast': mixed_contrast(table(actor_context)),
        'same_event_records': len(archive),
        'same_event_families': event_family_count(archive),
        'shared_demonstration_warning': (
            'Copies on different branches are the same implementation, '
            'not independent corroboration.'),
    }


class StructuralChecks(unittest.TestCase):
    def test_baseline_does_not_identify_generator(self):
        self.assertEqual(survivors({(0, 0): 0, (1, 0): 1}),
                         ['actor_only', 'actor_context'])

    def test_one_discriminating_holdout_can_split_rivals(self):
        self.assertEqual(survivors({(0, 0): 0, (1, 0): 1, (0, 1): 1}),
                         ['actor_context'])

    def test_null_observation_does_not_split_rivals(self):
        self.assertEqual(survivors({(0, 0): 0}),
                         ['actor_only', 'actor_context'])

    def test_mutation_erasing_context_is_detected(self):
        self.assertNotEqual(actor_only(0, 1), actor_context(0, 1))

    def test_complete_factorial_contrast(self):
        self.assertEqual(mixed_contrast(table(actor_context)), -2)

    def test_every_missing_corner_is_rejected(self):
        full = table(actor_context)
        for corner in CORNERS:
            with self.subTest(corner=corner), self.assertRaises(ValueError):
                mixed_contrast({k: v for k, v in full.items() if k != corner})

    def test_extra_corner_is_rejected(self):
        with self.assertRaises(ValueError):
            mixed_contrast(table(actor_context) | {(2, 0): 0})

    def test_norm_change_can_change_evaluation_not_observation(self):
        observed = 1
        allowed_under_first_norm = {0, 1}
        allowed_under_second_norm = {0}
        self.assertTrue(observed in allowed_under_first_norm)
        self.assertFalse(observed in allowed_under_second_norm)
        self.assertEqual(observed, 1)

    def test_identical_baseline_output_need_not_mean_identical_generator(self):
        self.assertEqual(actor_only(1, 0), actor_context(1, 0))
        self.assertNotEqual(table(actor_only), table(actor_context))

    def test_description_richness_does_not_add_observations(self):
        base = {(0, 0): 0}
        for richness in (0, 1, 10, 100):
            description = ' ' .join(f'detail-{j}' for j in range(richness))
            self.assertIsInstance(description, str)
            self.assertEqual(len(survivors(base)), 2)

    def test_multiple_edits_do_not_become_multiple_events(self):
        records = [Record('A', 'E', 'edit'), Record('B', 'E', 'edit')]
        self.assertEqual(event_family_count(records), 1)

    def test_new_event_is_new_provenance_not_automatically_truth(self):
        records = [Record('A', 'E', 'edit'), Record('B', 'F', 'raw')]
        self.assertEqual(event_family_count(records), 2)

    def test_prediction_does_not_choose_a_policy(self):
        prediction = {'person_says_no': True}
        respect = (prediction, 'stop')
        exploit = (prediction, 'continue_pressuring')
        self.assertEqual(respect[0], exploit[0])
        self.assertNotEqual(respect[1], exploit[1])

    def test_invalid_bit_is_rejected(self):
        for value in (2, -1, True, 0.0, '1'):
            with self.subTest(value=value), self.assertRaises(ValueError):
                bit(value)

    def test_event_record_identity_is_not_event_independence(self):
        a, b = Record('A', 'E', 'edit'), Record('B', 'E', 'edit')
        self.assertNotEqual(a, b)
        self.assertEqual(a.event_family, b.event_family)

    def test_impossible_data_can_refute_both_candidates(self):
        self.assertEqual(survivors({(0, 0): 1}), [])


if __name__ == '__main__':
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(StructuralChecks)
    result = unittest.TextTestRunner(stream=sys.stderr, verbosity=2).run(suite)
    payload = report()
    payload['test_summary'] = {
        'tests_run': result.testsRun,
        'failures': len(result.failures),
        'errors': len(result.errors),
        'successful': result.wasSuccessful(),
    }
    print(json.dumps(payload, indent=2, sort_keys=True))
    sys.exit(0 if result.wasSuccessful() else 1)
