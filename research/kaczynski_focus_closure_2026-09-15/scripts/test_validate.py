"""Mutation controls for the package checker, not tests of human psychology."""
import copy
import json
import re
import unittest
from validate import ROOT, chronology_relation, parse_date, validate_data


class PackageChecks(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT / 'data/evidence.json').read_text())
        self.sources = set(re.findall(r'^## ([STL]\d{2})\b', (ROOT / 'SOURCES.md').read_text(), re.M))
        self.claims = set(re.findall(r'^## (C\d{2})\b', (ROOT / 'CLAIM_LEDGER.md').read_text(), re.M))

    def errors(self, data=None):
        return validate_data(self.data if data is None else data, self.sources, self.claims)

    def test_positive_baseline(self):
        self.assertEqual(self.errors(), [])

    def test_null_unknown_dates_remain_legal(self):
        self.data['records'][8]['event_date'] = None
        self.data['records'][8]['report_date'] = None
        self.assertEqual(self.errors(), [])
        self.assertEqual(chronology_relation(None, '1978'), 'ambiguous')

    def test_same_year_order_is_not_invented(self):
        self.assertEqual(chronology_relation('1978-01', '1978-12'), 'ambiguous')

    def test_duplicate_record_rejected(self):
        self.data['records'].append(copy.deepcopy(self.data['records'][0]))
        self.assertTrue(any('duplicate' in e for e in self.errors()))

    def test_unknown_source_rejected(self):
        self.data['records'][0]['source'] = 'S99'
        self.assertTrue(any('unknown source' in e for e in self.errors()))

    def test_unknown_claim_rejected(self):
        self.data['records'][0]['claim'] = 'C99'
        self.assertTrue(any('unknown claim' in e for e in self.errors()))

    def test_report_event_swap_rejected(self):
        self.data['records'][3]['event_date'] = '1999'
        self.data['records'][3]['report_date'] = '1983'
        self.assertTrue(any('precedes' in e for e in self.errors()))

    def test_origin_date_mutation_requires_rewrite(self):
        self.data['records'][3]['event_date'] = '1973'
        self.assertTrue(any('C03 requires' in e for e in self.errors()))

    def test_invalid_calendar_date_rejected(self):
        with self.assertRaises(ValueError):
            parse_date('1983-02-31')

    def test_numeric_coordinates_rejected(self):
        self.data['records'][0]['coordinates'] = {'rho': 0.9}
        self.assertTrue(any('numerical' in e for e in self.errors()))

    def test_unknown_is_not_undefined_phi(self):
        self.data['records'][0]['analyst_pathway_state'] = 'subject_phi_undefined'
        self.assertTrue(any('undefined-phi' in e for e in self.errors()))

    def test_relabeling_development_as_holdout_rejected(self):
        self.data['records'][0]['development_set'] = False
        self.assertTrue(any('holdout' in e for e in self.errors()))

    def test_promoting_observation_to_causation_rejected(self):
        self.data['records'][0]['status'] = 'CORROBORATED_CAUSE'
        self.assertTrue(any('promoted' in e for e in self.errors()))

    def test_non_object_and_empty_records_rejected(self):
        self.assertTrue(self.errors([]))
        self.data['records'] = []
        self.assertTrue(self.errors())


if __name__ == '__main__':
    unittest.main()
