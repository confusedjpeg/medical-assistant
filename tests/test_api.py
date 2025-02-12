import unittest
from src.api.drug_interactions import fetch_drug_interaction_data
from src.api.medicine_data import get_medicine_data

class TestAPI(unittest.TestCase):

    def test_fetch_drug_interaction_data(self):
        # Test fetching drug interaction data
        response = fetch_drug_interaction_data('Aspirin', 'Ibuprofen')
        self.assertIsInstance(response, dict)
        self.assertIn('interactions', response)

    def test_get_medicine_data(self):
        # Test retrieving medicine data
        response = get_medicine_data('Aspirin')
        self.assertIsInstance(response, dict)
        self.assertIn('name', response)
        self.assertIn('uses', response)

if __name__ == '__main__':
    unittest.main()