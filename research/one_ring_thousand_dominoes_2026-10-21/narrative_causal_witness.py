"""Finite consistency witness: narrative, causal source, and action can diverge.

Research-tier synthetic example. NOT a model of a human brain, culture, or TLICA
foundation; no psychological, evolutionary, or organizational validation follows.

Run: python3 narrative_causal_witness.py
"""
from dataclasses import dataclass
import itertools
import unittest


@dataclass(frozen=True)
class History:
    u: int  # world cause channel 1
    v: int  # world cause channel 2; also a non-narrative action input

    def __post_init__(self):
        if self.u not in (0, 1) or self.v not in (0, 1):
            raise ValueError("binary toy history required")


def observation(h: History) -> int:
    """Lossy contact/substrate channel."""
    return h.u ^ h.v


def narrative(h: History, frame: int = 0) -> int:
    """Interpretive frame acts on an observation, not on the whole history."""
    if frame not in (0, 1):
        raise ValueError("binary frame required")
    return observation(h) ^ frame


def action(h: History, frame: int = 0, *,
           use_narrative: bool = True, use_non_narrative: bool = True) -> int:
    """Future action receives independent narrative and non-narrative paths."""
    n = narrative(h, frame) if use_narrative else 0
    z = h.v if use_non_narrative else 0
    return n ^ z


def observed_task(h: History, task: str) -> int:
    """A task family can distinguish histories overlooked by another."""
    if task == "visible":
        return h.u
    if task == "extended":
        return h.u ^ h.v
    raise ValueError("unknown task")


class TestNarrativeCausalWitness(unittest.TestCase):
    def test_positive_collision_same_narrative_different_world(self):
        h1, h2 = History(0, 0), History(1, 1)
        self.assertNotEqual(h1, h2)
        self.assertEqual(observation(h1), observation(h2))
        self.assertEqual(narrative(h1), narrative(h2))

    def test_positive_same_world_different_frames(self):
        h = History(0, 1)
        self.assertNotEqual(narrative(h, 0), narrative(h, 1))

    def test_distinct_actions_under_same_narrative(self):
        h1, h2 = History(0, 0), History(1, 1)
        self.assertEqual(narrative(h1), narrative(h2))
        self.assertNotEqual(action(h1), action(h2))

    def test_frame_intervention_alters_action_with_fixed_world(self):
        h = History(0, 1)
        self.assertEqual(observation(h), observation(h))
        self.assertNotEqual(action(h, 0), action(h, 1))

    def test_negative_control_without_narrative_route(self):
        for u, v in itertools.product((0, 1), repeat=2):
            h = History(u, v)
            self.assertEqual(action(h, 0, use_narrative=False),
                             action(h, 1, use_narrative=False))

    def test_mutation_control_toggle_frame(self):
        for u, v in itertools.product((0, 1), repeat=2):
            h = History(u, v)
            self.assertEqual(narrative(h, 1), 1 - narrative(h, 0))

    def test_non_narrative_ablation(self):
        h1, h2 = History(0, 0), History(1, 1)
        self.assertEqual(action(h1, use_non_narrative=False),
                         action(h2, use_non_narrative=False))

    def test_null_control_repeated_state(self):
        h = History(1, 0)
        self.assertEqual((observation(h), narrative(h, 0), action(h, 0)),
                         (observation(h), narrative(h, 0), action(h, 0)))

    def test_task_relative_indistinguishability(self):
        h1, h2 = History(0, 0), History(0, 1)
        self.assertEqual(observed_task(h1, "visible"),
                         observed_task(h2, "visible"))
        self.assertNotEqual(observed_task(h1, "extended"),
                            observed_task(h2, "extended"))

    def test_exhaustive_frame_coverage(self):
        counts = {}
        for u, v, frame in itertools.product((0, 1), repeat=3):
            h = History(u, v)
            key = (observation(h), narrative(h, frame), action(h, frame))
            counts[key] = counts.get(key, 0) + 1
        self.assertEqual(sum(counts.values()), 8)
        self.assertTrue(all(v > 0 for v in counts.values()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
