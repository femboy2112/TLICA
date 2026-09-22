"""Calibration and mutation controls; same-author tests, not independent validation."""
import copy
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

import transport_probe as p


class TransportTests(unittest.TestCase):
    def setUp(self):
        self.raw = p.fixture()
        self.source = p.Episode.parse(self.raw)
        self.identity = {node: node for node in self.source.nodes}

    def report(self, target=None, mapping=None):
        return p.assess(self.source, p.Episode.parse(target if target is not None else self.raw),
                        self.identity if mapping is None else mapping)

    def invalid(self, raw):
        with self.assertRaises(ValueError):
            p.Episode.parse(raw)

    def test_identity(self):
        self.assertEqual(self.report()["counts"], {"matched": 4, "contradicted": 0, "unknown": 0})

    def test_surface_change(self):
        for node in self.raw["nodes"]:
            node["label"] = "different " + node["label"]
        report = self.report(self.raw)
        self.assertEqual(report["equal_surface_labels"], 0)
        self.assertEqual(report["status"], "supported_on_scope")

    def test_same_labels_opposite_fact(self):
        self.raw["facts"][-1][-1] = -1
        report = self.report(self.raw)
        self.assertEqual(report["equal_surface_labels"], 4)
        self.assertEqual(report["counts"]["contradicted"], 1)

    def test_missing_is_unknown(self):
        self.raw["facts"].pop()
        report = self.report(self.raw)
        self.assertEqual(report["status"], "unresolved_on_scope")
        self.assertEqual(report["counts"]["contradicted"], 0)

    def test_reverse_is_not_negation(self):
        row = self.raw["facts"][-1]
        row[0], row[2] = row[2], row[0]
        report = self.report(self.raw)
        self.assertEqual(report["counts"]["unknown"], 1)
        self.assertEqual(report["counts"]["contradicted"], 0)
        self.assertEqual(report["reverse_only_count"], 1)

    def test_noninjective_rejected(self):
        with self.assertRaises(ValueError):
            self.report(mapping={"a": "k", "k": "k"})

    def test_type_mismatch_rejected(self):
        with self.assertRaises(ValueError):
            self.report(mapping={"a": "w"})

    def test_unknown_source_rejected(self):
        with self.assertRaises(ValueError):
            self.report(mapping={"ghost": "k"})

    def test_unknown_target_rejected(self):
        with self.assertRaises(ValueError):
            self.report(mapping={"a": "ghost"})

    def test_duplicate_node_rejected(self):
        self.raw["nodes"].append(copy.deepcopy(self.raw["nodes"][0]))
        self.invalid(self.raw)

    def test_duplicate_fact_rejected(self):
        self.raw["facts"].append(copy.deepcopy(self.raw["facts"][0]))
        self.invalid(self.raw)

    def test_conflicting_fact_rejected(self):
        row = copy.deepcopy(self.raw["facts"][0])
        row[-1] = -1
        self.raw["facts"].append(row)
        self.invalid(self.raw)

    def test_boolean_polarity_rejected(self):
        self.raw["facts"][0][-1] = True
        self.invalid(self.raw)

    def test_zero_polarity_rejected(self):
        self.raw["facts"][0][-1] = 0
        self.invalid(self.raw)

    def test_dangling_edge_rejected(self):
        self.raw["facts"][0][0] = "ghost"
        self.invalid(self.raw)

    def test_unknown_schema_key_rejected(self):
        self.raw["confidence"] = 0.99
        self.invalid(self.raw)

    def test_missing_provenance_rejected(self):
        self.raw["provenance"] = ""
        self.invalid(self.raw)

    def test_empty_map_is_not_support(self):
        self.assertEqual(self.report(mapping={})["status"], "insufficient_evidence")

    def test_partial_coverage_remains_visible(self):
        report = self.report(mapping={"a": "a", "w": "w"})
        self.assertEqual(report["status"], "supported_on_scope")
        self.assertEqual(report["fact_coverage"]["source_tested"], 1)
        self.assertEqual(report["fact_coverage"]["source_untested"], 3)

    def test_target_extras_not_equivalence(self):
        self.raw["facts"].append(["k", "cares_for", "a", 1])
        report = self.report(self.raw)
        self.assertEqual(report["status"], "supported_on_scope")
        self.assertEqual(report["fact_coverage"]["target_unexamined"], 1)

    def test_common_basis_required(self):
        self.raw["basis"] = "different-definition-of-care"
        with self.assertRaises(ValueError):
            self.report(self.raw)

    def test_partial_composition(self):
        self.assertEqual(p.compose_maps({"a": "x", "k": "y"}, {"x": "z"}), {"a": "z"})

    def test_composition_associativity(self):
        f, g, h = {"a": "x", "k": "y"}, {"x": "b", "y": "c"}, {"b": "q"}
        self.assertEqual(p.compose_maps(p.compose_maps(f, g), h), p.compose_maps(f, p.compose_maps(g, h)))

    def test_complete_factorial_and_stress_checks(self):
        result = p.calibration()
        self.assertEqual(len(result["factorial_cells"]), 4)
        self.assertEqual(result["renamings_checked"], 24)
        self.assertEqual(result["single_fact_polarity_mutations_detected"], 4)
        cases = {(row["surface_same"], row["structure_same"]) for row in result["factorial_cells"]}
        self.assertEqual(len(cases), 4)

    def test_counterfactual_nonidentifiability(self):
        result = p.calibration()["counterfactual_counterexample"]
        self.assertTrue(result["observed_outcomes_equal"])
        self.assertFalse(result["unobserved_outcomes_equal"])

    def test_duplicate_json_key_rejected(self):
        with self.assertRaises(ValueError):
            json.loads('{"map": {}, "map": {}}', object_pairs_hook=p.reject_duplicate_keys)

    def test_cli_input_roundtrip(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "input.json"
            target = Path(directory) / "output.json"
            source.write_text(json.dumps({"source": self.raw, "target": self.raw, "map": self.identity}), encoding="utf-8")
            result = subprocess.run([sys.executable, str(Path(p.__file__)), "--input", str(source), "--output", str(target)],
                                    capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertEqual(json.loads(target.read_text(encoding="utf-8"))["status"], "supported_on_scope")

    def test_cli_malformed_input_fails(self):
        with tempfile.TemporaryDirectory() as directory:
            source = Path(directory) / "bad.json"
            source.write_text('{"source": 1}', encoding="utf-8")
            result = subprocess.run([sys.executable, str(Path(p.__file__)), "--input", str(source)],
                                    capture_output=True, text=True, check=False)
            self.assertEqual(result.returncode, 2)
            self.assertIn("requires exactly", result.stderr)


if __name__ == "__main__":
    unittest.main(verbosity=2)
