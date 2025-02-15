import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.feature_extraction.text import CountVectorizer

from src.api.medicine_data import get_medicine_data
from src.api.drug_interactions import DrugInteractionChecker

class MedicalAssistantModel:
    def __init__(self):
        self.model = LogisticRegression()
        self.vectorizer = CountVectorizer()
        self.drug_checker = DrugInteractionChecker()

    def train(self, X, y):
        X_vec = self.vectorizer.fit_transform(X)
        self.model.fit(X_vec, y)
    
    def predict(self, symptoms):
        X_vec = self.vectorizer.transform(symptoms)
        predicted_medicines = self.model.predict(X_vec)
        
        # Retrieve medicine details and check for interactions
        medicine_details = [get_medicine_data(med) for med in predicted_medicines]
        interactions = self._check_interactions(predicted_medicines)
        
        return predicted_medicines, medicine_details, interactions
    
    def _check_interactions(self, medicines):
        interactions = []
        for i, med1 in enumerate(medicines):
            for med2 in medicines[i+1:]:
                interaction = self.drug_checker.check_interaction(med1, med2)
                if interaction:
                    interactions.append({
                        'drug1': med1,
                        'drug2': med2,
                        'effect': interaction
                    })
        return interactions
    
    def evaluate(self, X_test, y_test):
        X_vec = self.vectorizer.transform(X_test)
        predictions = self.model.predict(X_vec)
        accuracy = accuracy_score(y_test, predictions)
        print(f"Model accuracy: {accuracy:.2f}")
        return accuracy