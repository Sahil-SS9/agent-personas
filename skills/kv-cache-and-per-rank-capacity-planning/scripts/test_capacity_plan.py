#!/usr/bin/env python3
"""Provider-free controls for the shipped capacity estimator."""
import copy
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('capacity_plan', ROOT/'scripts/capacity_plan.py')
assert SPEC is not None and SPEC.loader is not None
MODULE = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MODULE)


class CapacityTests(unittest.TestCase):
    def setUp(self):
        self.data = json.loads((ROOT/'templates/gqa-capacity.json').read_text())

    def test_valid_fixture(self):
        result = MODULE.plan(self.data)
        self.assertTrue(result['estimated_admissible'])
        self.assertEqual(result['status'], 'estimate-only')
        # Independent tensor-shape count, using repeated dimensions.
        size = 1
        for dim in [32, 4, 128, 8192, 2, 2, 2]:
            size *= dim
        import decimal
        expected = int((decimal.Decimal(size)*decimal.Decimal('1.1')).to_integral_value(rounding=decimal.ROUND_CEILING))
        self.assertEqual(result['ranks'][0]['kv_bytes'], expected)

    def test_each_rank_not_aggregate(self):
        self.data['ranks'][0]['available_bytes'] = 1
        self.data['ranks'][1]['available_bytes'] *= 10
        self.assertFalse(MODULE.plan(self.data)['estimated_admissible'])

    def test_below_required_context(self):
        self.data['proposed_context'] = 4096
        self.assertFalse(MODULE.plan(self.data)['estimated_admissible'])

    def test_unsupported_architecture(self):
        for arch in ['mla', 'hybrid', 'sliding', None]:
            with self.subTest(arch=arch), self.assertRaises(ValueError):
                data=copy.deepcopy(self.data);data['architecture']=arch;MODULE.plan(data)

    def test_invalid_numbers(self):
        for value in [True, -1, 0, float('nan'), float('inf'), '8192', 8192.5]:
            with self.subTest(value=value), self.assertRaises(ValueError):
                data=copy.deepcopy(self.data);data['proposed_context']=value;MODULE.plan(data)

    def test_missing_budget(self):
        del self.data['ranks'][0]['workspace_bytes']
        with self.assertRaises(KeyError):MODULE.plan(self.data)

    def test_no_ranks(self):
        self.data['ranks']=[]
        with self.assertRaises(ValueError):MODULE.plan(self.data)

    def test_sharing_not_invented(self):
        self.data['kv_layout_multiplier']=0.5
        with self.assertRaises(ValueError):MODULE.plan(self.data)

    def test_cli_contract(self):
        proc=subprocess.run([sys.executable,str(ROOT/'scripts/capacity_plan.py'),str(ROOT/'templates/gqa-capacity.json')],capture_output=True,text=True)
        self.assertEqual(proc.returncode,0)
        self.assertTrue(json.loads(proc.stdout)['estimated_admissible'])

    def test_cli_invalid_json(self):
        with tempfile.TemporaryDirectory() as directory:
            p=Path(directory)/'bad.json';p.write_text('{broken')
            proc=subprocess.run([sys.executable,str(ROOT/'scripts/capacity_plan.py'),str(p)],capture_output=True,text=True)
            self.assertEqual(proc.returncode,2)
            self.assertEqual(json.loads(proc.stdout)['status'],'invalid-input')


if __name__=='__main__':
    unittest.main()
