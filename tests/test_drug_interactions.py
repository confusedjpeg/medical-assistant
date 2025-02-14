import unittest
from src.api.drug_interactions import DrugInteractionChecker

class TestDrugInteractions(unittest.TestCase):
    def setUp(self):
        self.checker = DrugInteractionChecker()

    def test_check_interaction(self):
        result = self.checker.check_interaction('Trioxsalen', 'Verteporfin')
        self.assertTrue(len(result) > 0)
        self.assertEqual(result[0], 'may increase the photosensitizing activities')

    def test_get_all_drugs(self):
        drugs = self.checker.get_all_drugs()
        self.assertIn('Verteporfin', drugs)
        self.assertIn('Trioxsalen', drugs)

if __name__ == '__main__':
    unittest.main()