import unittest
import os
import sys

# Add project root to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from src.api.drug_interactions import DrugInteractionChecker

class TestDrugInteractions(unittest.TestCase):
    def setUp(self):
        self.checker = DrugInteractionChecker()

    def test_check_interaction(self):
        result = self.checker.check_interaction('Trioxsalen', 'Verteporfin')
        self.assertTrue(len(result) > 0)
        self.assertEqual(result[0], 'Trioxsalen may increase the photosensitizing activities of Verteporfin.')

    def test_get_all_drugs(self):
        drugs = self.checker.get_all_drugs()
        self.assertIn('Verteporfin', drugs)
        self.assertIn('Trioxsalen', drugs)

if __name__ == '__main__':
    unittest.main()