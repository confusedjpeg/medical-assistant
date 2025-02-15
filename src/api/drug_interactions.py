import pandas as pd
import os

class DrugInteractionChecker:
    def __init__(self):
        self.drug_data = self._load_drug_data()
    
    def _load_drug_data(self):
        csv_path = os.path.join(os.path.dirname(__file__), 'data', 'drug_interactions.csv')
        try:
            return pd.read_csv(csv_path)
        except FileNotFoundError:
            print("Drug interaction data file not found")
            return pd.DataFrame()

    def check_interaction(self, drug1, drug2):
        interactions = self.drug_data[
            ((self.drug_data['drug1'].str.lower() == drug1.lower()) & 
             (self.drug_data['drug2'].str.lower() == drug2.lower())) |
            ((self.drug_data['drug1'].str.lower() == drug2.lower()) & 
             (self.drug_data['drug2'].str.lower() == drug1.lower()))
        ]
        return interactions['interaction_effect'].tolist() if not interactions.empty else []

    def get_drug_info(self, drug_name):
        drug_info = self.drug_data[self.drug_data['drug1'] == drug_name]
        return drug_info.to_dict('records') if not drug_info.empty else {}

    def get_all_drugs(self):
        return list(set(self.drug_data['drug1'].tolist() + self.drug_data['drug2'].tolist()))

def get_interaction_recommendations(drug_list):
    checker = DrugInteractionChecker()
    interactions = []
    
    for i, drug1 in enumerate(drug_list):
        for drug2 in drug_list[i+1:]:
            interaction = checker.check_interaction(drug1, drug2)
            if interaction:
                interactions.append({
                    'drug1': drug1,
                    'drug2': drug2,
                    'effect': interaction[0]
                })
    
    return interactions