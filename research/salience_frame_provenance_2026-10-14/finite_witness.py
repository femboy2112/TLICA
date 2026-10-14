#!/usr/bin/env python3
"""Finite construction checks for TLICA salience/frame/provenance research.

These are deterministic checks of formal definitions, NOT tests on humans.
No external dependencies, private data, model inference, or I/O beyond test output.
"""

from itertools import product
import unittest


def local_admissible(before: int, after: int) -> bool:
    """A step is locally small, but no global guard is consulted."""
    return abs(after - before) <= 1


def frozen_global_guard(start: int, after: int) -> bool:
    """Forbid total warning-weight drift larger than one unit."""
    return after >= start - 1


def fixed_invariant(state: int) -> int:
    return state % 2


def retains_fixed_invariant(path: tuple[int, ...]) -> bool:
    return all(fixed_invariant(a) == fixed_invariant(b)
               for a, b in zip(path, path[1:]))


def summarize_history(history: tuple[str, ...]) -> str:
    """Deliberately lossy: retain endpoint only."""
    return history[-1]


def threshold_action(known: bool, intrinsic: int, context: int,
                     urgency: int, resistance: int, threshold: int = 1) -> bool:
    """Illustrative action predicate. Not a model of any person's cognition."""
    return bool(known and intrinsic + context + urgency - resistance >= threshold)


class FormalChecks(unittest.TestCase):
    def test_fixed_invariant_preserves_under_composition(self):
        # Exhaustive finite check: any length-four binary-valued path whose
        # every edge preserves parity also preserves its endpoint parity.
        for path in product(range(4), repeat=4):
            if retains_fixed_invariant(path):
                self.assertEqual(fixed_invariant(path[0]),
                                 fixed_invariant(path[-1]))

    def test_mutant_breaks_invariant_and_is_detected(self):
        mutant = (0, 2, 3, 5)  # one edge changes parity
        self.assertFalse(retains_fixed_invariant(mutant))

    def test_local_steps_can_violate_distinct_global_guard(self):
        path = (4, 3, 2, 1, 0)
        self.assertTrue(all(local_admissible(a, b)
                            for a, b in zip(path, path[1:])))
        self.assertFalse(local_admissible(path[0], path[-1]))
        self.assertFalse(frozen_global_guard(path[0], path[-1]))

    def test_frozen_guard_blocks_bypass(self):
        path = (4, 3, 2, 1, 0)
        self.assertFalse(all(frozen_global_guard(path[0], state)
                             for state in path[1:]))
        self.assertTrue(frozen_global_guard(4, 3))

    def test_lossy_provenance_collides(self):
        supported = ('checked-source', 'accepted', 'final-frame')
        unsupported = ('ignored-source', 'accepted', 'final-frame')
        self.assertNotEqual(supported, unsupported)
        self.assertEqual(summarize_history(supported),
                         summarize_history(unsupported))
        # Mutation/positive-control: exposing the full log distinguishes them.
        self.assertNotEqual(tuple(supported), tuple(unsupported))

    def test_possession_does_not_force_activation(self):
        known = True
        self.assertFalse(threshold_action(known, 0, 0, 0, 1))
        self.assertTrue(threshold_action(known, 0, 2, 0, 1))
        self.assertTrue(threshold_action(known, 0, 0, 2, 1))
        # A merely declared, renegotiable deadline adds zero real urgency.
        self.assertFalse(threshold_action(known, 0, 0, 0, 1))

    def test_noop_is_null_control(self):
        self.assertTrue(local_admissible(3, 3))
        self.assertTrue(frozen_global_guard(4, 4))
        self.assertEqual(summarize_history(('x', 'state')),
                         summarize_history(('y', 'state')))


if __name__ == '__main__':
    unittest.main(verbosity=2)
