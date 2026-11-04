"""Known-answer and rejection tests for capacity_estimate.py (stdlib unittest)."""
import json, subprocess, sys, tempfile, unittest
from pathlib import Path

SCRIPT = Path(__file__).with_name('capacity_estimate.py')


def run(data):
    with tempfile.NamedTemporaryFile('w', suffix='.json', delete=False) as fh:
        json.dump(data, fh)
    p = subprocess.run([sys.executable, str(SCRIPT), fh.name], capture_output=True, text=True)
    return p.returncode, json.loads(p.stdout)


def fig(result, name):
    return next(f['value'] for f in result['figures'] if f['figure'] == name)


class KnownAnswers(unittest.TestCase):
    def test_public_microblog_exercise(self):
        # 150M DAU, 2 posts/day, 10% with 1 MB media, 5-year retention: ~3.5K write QPS, 30 TB/day, ~55 PB.
        code, r = run({'traffic': {'dau': 1.5e8, 'actions_per_user_per_day': {'write': 2}, 'peak_factor': 2},
                       'storage': {'objects': [{'name': 'media', 'bytes_per_write': 1e6, 'fraction_of_writes': 0.1}],
                                   'retention_days': 1825, 'replication_factor': 3}})
        self.assertEqual(code, 0)
        self.assertAlmostEqual(fig(r, 'write_qps_avg'), 3472.2, places=0)
        self.assertAlmostEqual(fig(r, 'write_qps_peak'), 6944.4, places=0)
        self.assertAlmostEqual(fig(r, 'storage_per_day_media'), 3.0e13, delta=1e9)
        self.assertAlmostEqual(fig(r, 'storage_raw_over_retention') / 1e15, 54.75, places=2)
        self.assertAlmostEqual(fig(r, 'storage_replicated') / 1e15, 164.25, places=2)

    def test_llm_tokens_and_cost(self):
        code, r = run({'llm': {'requests_per_s_avg': 10, 'peak_factor': 3, 'input_tokens': 2000, 'output_tokens': 500,
                               'output_tokens_per_s_per_replica': 1000, 'target_utilisation': 0.5,
                               'usd_per_million_input': 3, 'usd_per_million_output': 15}})
        self.assertEqual(code, 0)
        self.assertEqual(fig(r, 'llm_output_tokens_per_s_peak'), 15000)
        self.assertEqual(fig(r, 'llm_replicas_for_peak'), 30)
        self.assertAlmostEqual(fig(r, 'llm_cost_per_request_usd'), 0.0135)
        self.assertAlmostEqual(fig(r, 'llm_cost_per_day_usd'), 11664.0)

    def test_failure_domain_headroom(self):
        code, r = run({'traffic': {'dau': 8.64e6, 'actions_per_user_per_day': {'read': 100}, 'peak_factor': 2},
                       'node': {'qps_per_node': 1000, 'target_utilisation': 0.5, 'failure_domains': 3}})
        self.assertEqual(fig(r, 'nodes_for_peak'), 40)
        self.assertEqual(fig(r, 'nodes_n_plus_one_domain'), 60)


class Rejections(unittest.TestCase):
    def test_missing_dau(self):
        code, r = run({'traffic': {'actions_per_user_per_day': {'write': 1}, 'peak_factor': 2}})
        self.assertEqual(code, 1)
        self.assertIn('missing-assumption: traffic.dau', r['errors'])

    def test_negative_value(self):
        code, r = run({'traffic': {'dau': -5, 'actions_per_user_per_day': {'write': 1}, 'peak_factor': 2}})
        self.assertEqual(code, 1)

    def test_empty(self):
        code, r = run({})
        self.assertEqual(code, 1)

    def test_warns_low_peak_and_single_copy(self):
        code, r = run({'traffic': {'dau': 1e6, 'actions_per_user_per_day': {'write': 1}, 'peak_factor': 1.0},
                       'storage': {'objects': [{'bytes_per_write': 100}], 'retention_days': 30, 'replication_factor': 1}})
        self.assertEqual(code, 0)
        self.assertTrue(any('peak_factor' in w for w in r['warnings']))
        self.assertTrue(any('replication_factor' in w for w in r['warnings']))


if __name__ == '__main__':
    unittest.main()
