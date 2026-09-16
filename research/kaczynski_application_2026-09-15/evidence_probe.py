#!/usr/bin/env python3
"""Finite construction checks and a selected-record dependency audit; NOT psychology.

Run: python3 evidence_probe.py --test
     python3 evidence_probe.py --output RAW_RESULTS.json
Only the named output file is written. No network, third-party modules, or source scraping.
"""
from __future__ import annotations
import argparse
import itertools
import json
import unittest
from fractions import Fraction as Q
from pathlib import Path
from typing import Callable, Hashable, Iterable

SOURCE_GROUPS = {
    'FBI': {'S01'}, 'manifesto': {'S03'}, 'interview': {'S04'},
    'prosecution_selection': {'S06'}, 'Fleming_research': {'S07', 'S13'},
}
# These are deliberately declared citation dependencies, not estimated causal edges.
CLAIM_REQUIREMENTS = {
    'D1_chronology_exclusion': {'S01', 'S04'},
    'D2_alternative_represented': {'S03'},
    'D3_early_revenge_record': {'S06'},
    'D4_later_harm_awareness': {'S04'},
    'D5_nonexclusive_motives_scholarly_argument': {'S07'},
    'D6_intellectual_genealogy_scholarly_argument': {'S13'},
}

def derivative(b: Q, f: Q, gamma: Q, rho: Q) -> Q:
    if not 0 <= b <= 1 or not 0 <= f <= 1 or not 0 <= rho <= 1 or gamma <= 0:
        raise ValueError('profile values must lie in [0,1], gamma must be positive')
    return gamma * (f - b)  # rho is a metric reading, not a factor in this law.

def partition(states: Iterable[Hashable], signature: Callable) -> list[list]:
    cells: dict[Hashable, list] = {}
    for state in states:
        cells.setdefault(signature(state), []).append(state)
    if not cells:
        raise ValueError('an empty domain supplies no construction witness')
    return list(cells.values())

def descends(cells: list[list], property_fn: Callable) -> bool:
    if not cells or any(not cell for cell in cells):
        raise ValueError('nonempty equivalence classes required')
    return all(len({property_fn(x) for x in cell}) == 1 for cell in cells)

def institutional_signature(state: tuple[str, bool, bool]) -> tuple[bool, bool]:
    _clerk, enabled, _consent = state
    return tuple(enabled and credential for credential in (False, True))

def support(available: set[str]) -> dict[str, bool]:
    return {claim: required <= available for claim, required in CLAIM_REQUIREMENTS.items()}

def results() -> dict:
    vals = [Q(i, 5) for i in range(1, 5)]
    tracking = []
    for b, f, gamma in itertools.product(vals, vals, (Q(1, 2), Q(1))):
        a, z = [derivative(b, f, gamma, rho) for rho in (Q(1, 4), Q(3, 4))]
        tracking.append({'b': str(b), 'f': str(f), 'gamma': str(gamma),
                         'rho_quarter': str(a), 'rho_three_quarters': str(z), 'equal': a == z})
    states = list(itertools.product(('A', 'B'), (False, True), (False, True)))
    cells = partition(states, institutional_signature)
    all_sources = set().union(*SOURCE_GROUPS.values())
    ablations = {'full_selected_set': support(all_sources)}
    for group, ids in SOURCE_GROUPS.items():
        ablations['without_' + group] = support(all_sources - ids)
    # All five non-institutional records have actor-level dependency, including scholarship.
    ablations['without_K_authored_or_dependent_records'] = support({'S01'})
    # The same descriptive input can be completed by incompatible normative rules.
    permission = [{'descriptive_input': 'same_stipulated_facts', 'normative_rule': rule,
                   'permission_for_h': permission} for rule, permission in
                  [('nonconsenting_person_veto', False), ('project_overrides_veto', True)]]
    # This is a formal observational-equivalence witness, not a fitted record of the actor.
    observation = {'selective_reader': [1, 1], 'open_reader_in_uniform_environment': [1, 1]}
    return {
        'scope': 'synthetic_constructions_and_declared_document_dependencies_only',
        'theory_snapshot': '33d449424dd909bab5dfe8e80f302df733bd2770',
        'phase1_snapshot': 'f436412733b39b15fd7c3394d6a5064e9b5dc39c',
        'tracking': {'matched_pairs': len(tracking), 'mismatches': sum(not x['equal'] for x in tracking),
                     'rows': tracking, 'anchor_derivative': str(derivative(Q(1), Q(1), Q(1), Q(1)))},
        'quotient': {'microstates': len(states), 'classes': len(cells), 'cells': cells,
                     'task_response_descends': descends(cells, institutional_signature),
                     'consent_property_descends': descends(cells, lambda x: x[2])},
        'truth_to_permission_countermodels': permission,
        'narrative_nonidentification_witness': observation,
        'document_support_ablation': ablations,
        'interpretation': 'Support means the declared cited records remain. It is NOT truth, effect size, or probability.',
        'historical_causal_validation': 'NOT_RUN', 'independent_coding': 'NOT_RUN',
        'whole_repository_make_validate': 'NOT_RUN_complete_checkout_unavailable',
    }

class Controls(unittest.TestCase):
    def test_tracking_positive(self):
        self.assertEqual(results()['tracking']['mismatches'], 0)
    def test_tracking_count(self):
        self.assertEqual(results()['tracking']['matched_pairs'], 32)
    def test_metric_force_mutation_detectable(self):
        b, f, g = Q(1, 5), Q(4, 5), Q(1, 2)
        self.assertNotEqual(Q(1, 4)*derivative(b,f,g,Q(1,4)), Q(3,4)*derivative(b,f,g,Q(3,4)))
    def test_field_change_has_effect(self):
        self.assertNotEqual(derivative(Q(1,5),Q(2,5),Q(1),Q(1,2)), derivative(Q(1,5),Q(4,5),Q(1),Q(1,2)))
    def test_anchor(self):
        self.assertEqual(derivative(Q(1), Q(1), Q(2), Q(1)), 0)
    def test_invalid_profile_rejected(self):
        with self.assertRaises(ValueError): derivative(Q(2),Q(0),Q(1),Q(1))
    def test_quotient_positive(self):
        self.assertTrue(results()['quotient']['task_response_descends'])
    def test_quotient_negative_transport(self):
        self.assertFalse(results()['quotient']['consent_property_descends'])
    def test_identity_partition_retains_property(self):
        states = list(itertools.product(('A','B'),(False,True),(False,True)))
        self.assertTrue(descends(partition(states, lambda x:x), lambda x:x[2]))
    def test_empty_domain_not_witness(self):
        with self.assertRaises(ValueError): partition([], lambda x:x)
    def test_empty_class_not_witness(self):
        with self.assertRaises(ValueError): descends([[]], lambda x:x)
    def test_full_record_support(self):
        self.assertTrue(all(support(set().union(*SOURCE_GROUPS.values())).values()))
    def test_null_sources(self):
        self.assertFalse(any(support(set()).values()))
    def test_interview_dependency(self):
        row = results()['document_support_ablation']['without_interview']
        self.assertFalse(row['D1_chronology_exclusion']); self.assertFalse(row['D4_later_harm_awareness'])
    def test_mirror_cannot_restore_source(self):
        available = set().union(*SOURCE_GROUPS.values()) - {'S04'}
        self.assertEqual(support(available), support(available | {'S04_mirror'}))
    def test_permission_not_determined(self):
        rows = results()['truth_to_permission_countermodels']
        self.assertEqual(rows[0]['descriptive_input'], rows[1]['descriptive_input'])
        self.assertNotEqual(rows[0]['permission_for_h'], rows[1]['permission_for_h'])

def main() -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--test', action='store_true')
    p.add_argument('--output', type=Path)
    a = p.parse_args()
    if a.test:
        run = unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Controls))
        if not run.wasSuccessful(): return 1
    payload = json.dumps(results(), indent=2, ensure_ascii=False) + '\n'
    if a.output: a.output.write_text(payload, encoding='utf-8')
    elif not a.test: print(payload, end='')
    return 0

if __name__ == '__main__':
    raise SystemExit(main())
