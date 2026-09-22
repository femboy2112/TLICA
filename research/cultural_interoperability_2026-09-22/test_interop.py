"""Calibration and hostile controls. Both implementations share one authoring run."""
from __future__ import annotations

import copy
import itertools
import random
import unittest

from fixtures import cases
from interop import conjunction, gate_matrix, predictive_overlap, solve, transport_report, validate


class InteroperabilityTests(unittest.TestCase):
    def setUp(self):
        self.cases = {case["id"]: case for case in cases()}
        self.workshop = self.cases["workshop"]

    def test_three_valued_truth_tables(self):
        # Separate set-based bounds oracle, exhaustive through six gates.
        for n in range(7):
            for values in itertools.product((True, False, None), repeat=n):
                known_failures = {i for i, v in enumerate(values) if v is False}
                unknowns = {i for i, v in enumerate(values) if v is None}
                expected = False if known_failures else None if unknowns else True
                self.assertIs(conjunction(list(values)), expected)

    def test_supported_frontier_not_one_winner(self):
        result = solve(self.workshop)
        self.assertEqual(result["supported_frontier"], ["schedule_a", "schedule_b"])
        self.assertEqual(result["supported"], ["costly_schedule", "schedule_a", "schedule_b"])

    def test_unsafe_joint_windfall_rejected(self):
        result = solve(self.workshop)
        self.assertIn("unsafe_windfall", result["rejected"])
        self.assertNotIn("unsafe_windfall", result["supported_frontier"])

    def test_unknown_evidence_not_infeasible(self):
        result = solve(self.cases["unmeasured_insulation"])
        self.assertEqual(result["status"], "UNRESOLVED")
        self.assertEqual(result["pending"], ["insulation"])
        self.assertEqual(result["minimal_blockers"], [])

    def test_measurement_repair_changes_verdict(self):
        case = self.cases["unmeasured_insulation"]
        case["sources"][1]["status"] = "confirmed"
        self.assertEqual(solve(case)["supported"], ["insulation"])

    def test_negative_measurement_changes_verdict(self):
        case = self.cases["unmeasured_insulation"]
        case["sources"][1]["status"] = "confirmed"
        case["options"][0]["checks"]["reality"] = False
        self.assertEqual(solve(case)["status"], "NO_PERMISSIBLE_OPTION_IN_CATALOG")

    def test_real_conflict_core(self):
        result = solve(self.cases["shared_map_real_conflict"])
        self.assertEqual(result["minimal_blockers"], [["constraint:floor_A", "constraint:floor_B"]])

    def test_consent_is_not_predicted_benefit(self):
        result = solve(self.cases["consent_withheld"])
        self.assertEqual(result["supported"], [])
        self.assertEqual(result["minimal_blockers"], [["consent:B"]])

    def test_pending_consent_stays_pending(self):
        case = self.cases["consent_withheld"]
        case["options"][0]["consent"]["B"] = None
        self.assertEqual(solve(case)["status"], "UNRESOLVED")

    def test_externalities_not_erased(self):
        self.assertEqual(solve(self.cases["third_party_cost"])["supported"], [])

    def test_music_not_necessary(self):
        self.assertTrue(solve(self.workshop)["supported"])
        self.assertEqual(solve(self.cases["music_as_one_probe"])["supported"], ["separate_headphones"])

    def test_pairwise_compatibility_is_insufficient(self):
        full = self.cases["pairwise_not_global"]
        for pair in itertools.combinations(full["parties"], 2):
            subset = copy.deepcopy(full)
            subset["parties"] = list(pair)
            subset["constraints"] = [c for c in subset["constraints"] if c["kind"] != "party_floor" or c["owner"] in pair]
            wanted = {c["id"] for c in subset["constraints"]}
            for o in subset["options"]:
                o["checks"] = {k: v for k, v in o["checks"].items() if k in wanted}
                for field in ("consent", "ranks"):
                    o[field] = {k: v for k, v in o[field].items() if k in pair}
            self.assertTrue(solve(subset)["supported"])
        self.assertEqual(solve(full)["minimal_blockers"], [["constraint:floor_A", "constraint:floor_B", "constraint:floor_C"]])

    def test_empty_catalog_is_pathway_gap(self):
        self.assertEqual(solve(self.cases["no_candidate_yet"])["status"], "EMPTY_CATALOG_PATHWAY_GAP")

    def test_source_family_ablation(self):
        result = solve(self.workshop, frozenset({"authored_fixture"}))
        self.assertEqual(result["supported"], [])
        self.assertEqual(result["status"], "UNRESOLVED")

    def test_source_duplication_does_not_add_support(self):
        case = self.cases["unmeasured_insulation"]
        result = solve(case)
        duplicate = copy.deepcopy(case["sources"][1])
        duplicate["id"] = "same_source_copy"
        case["sources"].append(duplicate)
        case["constraints"][0]["source_ids"].append("same_source_copy")
        self.assertEqual(solve(case)["supported"], result["supported"])
        self.assertEqual(solve(case)["pending"], result["pending"])

    def test_relabeling_preserves_options(self):
        case = copy.deepcopy(self.workshop)
        case["description"] = "Different surface story; all declared gates unchanged."
        self.assertEqual(solve(case), solve(self.workshop))

    def test_separate_monotone_rank_transforms(self):
        expected = solve(self.workshop)["supported_frontier"]
        for option in self.workshop["options"]:
            option["ranks"]["A"] = 7 * option["ranks"]["A"] + 13
            option["ranks"]["B"] = 3 * option["ranks"]["B"] - 500
        self.assertEqual(solve(self.workshop)["supported_frontier"], expected)

    def test_candidate_order_does_not_choose_winner(self):
        expected = solve(self.workshop)
        self.workshop["options"].reverse()
        self.assertEqual(solve(self.workshop), expected)

    def test_missing_consent_rejected_as_input(self):
        del self.workshop["options"][0]["consent"]["A"]
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_duplicate_option_rejected(self):
        self.workshop["options"].append(copy.deepcopy(self.workshop["options"][0]))
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_fake_boolean_rejected(self):
        self.workshop["options"][0]["consent"]["A"] = 1
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_unknown_source_id_rejected(self):
        self.workshop["constraints"][0]["source_ids"] = ["missing"]
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_live_people_inputs_disabled(self):
        self.workshop["kind"] = "human"
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_standing_gate_cannot_be_omitted(self):
        self.workshop["constraints"] = [c for c in self.workshop["constraints"] if c["kind"] != "standing"]
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_transport_preserves_relations(self):
        report = transport_report([["a", "needs", "t"]], [["b", "needs", "u"]], {"a": "b", "t": "u"})
        self.assertTrue(report["exact_on_declared_graphs"])

    def test_transport_detects_reversed_relation(self):
        report = transport_report([["a", "needs", "t"]], [["u", "needs", "b"]], {"a": "b", "t": "u"})
        self.assertFalse(report["preserves_declared_edges"])

    def test_transport_does_not_erase_extra_history(self):
        report = transport_report([["a", "needs", "t"]], [["b", "needs", "u"], ["b", "remembers", "h"]], {"a": "b", "t": "u"})
        self.assertTrue(report["preserves_declared_edges"])
        self.assertFalse(report["exact_on_declared_graphs"])
        self.assertEqual(len(report["extra_edges"]), 1)

    def test_empty_transport_not_success(self):
        with self.assertRaises(ValueError):
            transport_report([], [], {})

    def test_noninjective_transport_rejected(self):
        with self.assertRaises(ValueError):
            transport_report([["a", "needs", "t"]], [["b", "needs", "b"]], {"a": "b", "t": "b"})

    def test_null_probe_splits_nothing(self):
        self.assertEqual(predictive_overlap({"m1": "same", "m2": "same", "m3": None})["split_pairs"], 0)

    def test_discriminating_probe_keeps_unknown_mass(self):
        result = predictive_overlap({"m1": "a", "m2": "b", "m3": None, "m4": "b"})
        self.assertEqual((result["split_pairs"], result["unresolved_pairs"], result["total_pairs"]), (2, 4, 6))

    def test_malformed_case_rejected(self):
        with self.assertRaises(ValueError):
            validate("not a case")

    def test_nonlist_source_references_rejected(self):
        self.workshop["constraints"][0]["source_ids"] = "stipulation"
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_nondict_consent_rejected(self):
        self.workshop["options"][0]["consent"] = ["A", "B"]
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_disputed_source_is_not_confirmed(self):
        self.workshop["sources"][0]["status"] = "disputed"
        self.assertEqual(solve(self.workshop)["status"], "UNRESOLVED")

    def test_reality_gate_cannot_be_omitted(self):
        self.workshop["constraints"] = [c for c in self.workshop["constraints"] if c["kind"] != "reality"]
        for o in self.workshop["options"]:
            del o["checks"]["reality"]
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_party_floor_cannot_be_omitted(self):
        self.workshop["constraints"] = [c for c in self.workshop["constraints"] if c["id"] != "floor_A"]
        for o in self.workshop["options"]:
            del o["checks"]["floor_A"]
        with self.assertRaises(ValueError):
            validate(self.workshop)

    def test_bounded_random_catalogs_against_set_oracle(self):
        # Configuration holdout, NOT independent sociological evidence.
        rng = random.Random(9222026)
        for _ in range(150):
            case = copy.deepcopy(self.workshop)
            for option in case["options"]:
                option["checks"] = {c["id"]: rng.choice((True, False, None)) for c in case["constraints"]}
                option["consent"] = {p: rng.choice((True, False, None)) for p in case["parties"]}
            matrix = gate_matrix(case)
            universe = set(matrix)
            failures = {oid for oid, row in matrix.items() if any(v is False for v in row.values())}
            uncertified = {oid for oid, row in matrix.items() if any(v is None for v in row.values())}
            result = solve(case)
            self.assertEqual(set(result["supported"]), universe - failures - uncertified)
            self.assertEqual(set(result["pending"]), uncertified - failures)
            for core in result["minimal_blockers"]:
                self.assertTrue(all(any(row[g] is False for g in core) for row in matrix.values()))
                for g in core:
                    smaller = set(core) - {g}
                    self.assertFalse(all(any(row[h] is False for h in smaller) for row in matrix.values()))


if __name__ == "__main__":
    unittest.main(verbosity=2)
