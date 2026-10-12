"""Unit tests of finite bookkeeping ONLY, not of TLICA or slang psychology."""
import unittest
from finite_lexicon import Rival, survivors, split_count, exact_classes, synthetic_cases


class FiniteLexiconTests(unittest.TestCase):
    def setUp(self):
        self.cases = synthetic_cases()

    def test_vibe_surface_cannot_identify_rapport(self):
        states = self.cases["vibe"]
        self.assertEqual(len(survivors(states, {"surface_label": "good_vibe"})), 2)
        self.assertEqual(split_count(states, "independent_report"), (1, 0))

    def test_coarse_label_is_not_unique_world_state(self):
        states = self.cases["vibe"]
        self.assertEqual(len(exact_classes(states, ("surface_label",))), 1)
        self.assertEqual(len(exact_classes(states, ("surface_label", "independent_report"))), 2)

    def test_cope_is_not_proof_of_defensiveness(self):
        states = self.cases["cope"]
        self.assertEqual(len(survivors(states, {"surface_token": "cope"})), 3)
        self.assertEqual(split_count(states, "speech_role"), (2, 1))

    def test_unknown_prediction_does_not_split(self):
        self.assertEqual(split_count(self.cases["cope"], "credible_counterevidence"), (1, 2))

    def test_adaptive_coping_is_consistent_with_revision(self):
        candidates = survivors(self.cases["cope"], {
            "speech_role": "self_description", "credible_counterevidence": "revises_belief"})
        self.assertEqual(tuple(c.name for c in candidates), ("adaptive_coping",))

    def test_absorption_alone_does_not_establish_disorientation(self):
        states = self.cases["lost_in_sauce"]
        self.assertEqual(len(survivors(states, {"high_immersion": "yes"})), 2)
        self.assertEqual(split_count(states, "checkpoint"), (1, 0))

    def test_information_refinement_cannot_expand_survivors(self):
        for states in self.cases.values():
            first = set(r.name for r in survivors(states, {}))
            for probe, outcome in states[0].predictions.items():
                if outcome is None:
                    continue
                new = set(r.name for r in survivors(states, {probe: outcome}))
                self.assertTrue(new <= first)

    def test_mutation_control_changes_conclusion(self):
        original = self.cases["lost_in_sauce"]
        changed = (original[0], Rival("absorbed_and_disoriented", {
            **original[1].predictions, "checkpoint": "goal_recovered"}))
        self.assertEqual(split_count(original, "checkpoint"), (1, 0))
        self.assertEqual(split_count(changed, "checkpoint"), (0, 1))

    def test_nonexistent_probe_cannot_distinguish(self):
        self.assertEqual(split_count(self.cases["vibe"], "not_run"), (0, 1))

    def test_partial_signatures_not_equivalence_proof(self):
        with self.assertRaises(ValueError):
            exact_classes(self.cases["cope"], ("credible_counterevidence",))


if __name__ == "__main__":
    unittest.main()
