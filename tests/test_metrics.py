import copy
import importlib.util
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('metrics', ROOT/'.agents/skills/video-production-director/scripts/analyze_metrics.py')
metrics = importlib.util.module_from_spec(spec)
spec.loader.exec_module(metrics)


class MetricsTests(unittest.TestCase):
    def setUp(self):
        self.row = dict(video_id='synthetic-test-only', observed_at='2026-10-24T08:00:00+00:00',
                        window_h='72', traffic_scope='unknown', metric_basis='fixture-not-platform-data',
                        plays='1000', shares='10', saves='', new_follows='5', qualified_leads='1',
                        settled_receipts='500', refunds='50', cash_cost='100', labor_hours='4', labor_rate='60', currency='CNY')

    def test_missing_metric_is_not_zero(self):
        result = metrics.analyze([self.row])
        self.assertTrue(result['passed'])
        self.assertIsNone(result['rows'][0]['events_per_1000_plays']['saves'])

    def test_zero_denominator_is_unknown(self):
        self.row['plays'] = '0'
        self.assertIsNone(metrics.analyze([self.row])['rows'][0]['events_per_1000_plays']['shares'])

    def test_cash_and_labor_are_distinct(self):
        row = metrics.analyze([self.row])['rows'][0]
        self.assertEqual(row['cash_contribution'], 350)
        self.assertEqual(row['labor_adjusted_contribution'], 110)

    def test_unknown_cost_blocks_contribution(self):
        self.row['cash_cost'] = ''
        self.assertIsNone(metrics.analyze([self.row])['rows'][0]['cash_contribution'])

    def test_different_windows_are_not_pooled(self):
        other = copy.deepcopy(self.row); other['window_h'] = '24'
        result = metrics.analyze([self.row, other])
        self.assertTrue(result['passed'])
        self.assertEqual(len(result['warnings']), 2)
        self.assertNotEqual(*[r['comparison_group'] for r in result['rows']])

    def test_duplicate_snapshot_rejected(self):
        self.assertFalse(metrics.analyze([self.row, self.row])['passed'])

    def test_nan_is_not_silently_accepted(self):
        self.row['settled_receipts'] = 'nan'
        self.assertFalse(metrics.analyze([self.row])['passed'])

    def test_paid_and_organic_are_separate(self):
        other = copy.deepcopy(self.row); other.update(video_id='second-fixture', traffic_scope='paid')
        result = metrics.analyze([self.row, other])
        self.assertTrue(result['warnings'])
        self.assertNotEqual(*[r['comparison_group'] for r in result['rows']])

    def test_currency_required(self):
        self.row['currency'] = ''
        self.assertFalse(metrics.analyze([self.row])['passed'])

    def test_counts_are_integer(self):
        self.row['plays'] = '2.5'
        self.assertFalse(metrics.analyze([self.row])['passed'])

    def test_empty_template_has_no_results(self):
        result = metrics.analyze([])
        self.assertEqual(result['rows'], [])
        self.assertTrue(result['warnings'])


if __name__ == '__main__':
    unittest.main()
