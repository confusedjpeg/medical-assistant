import os
import pandas as pd
import joblib
from src.ml.model import MedicalAssistantModel

def train_model():
    """
    Train the machine learning model using the provided data and labels.
    
    Returns:
    - model: The trained machine learning model.
    """
    # Load training data
    data_path = os.path.join(os.path.dirname(__file__), 'data', 'training_data.csv')
    training_data = pd.read_csv(data_path)
    
    X = training_data['symptoms'].tolist()
    y = training_data['medicine'].tolist()
    
    # Initialize and train the model
    model = MedicalAssistantModel()
    model.train(X, y)
    
    # Evaluate the model
    X_test, y_test = X[:10], y[:10]  # Example test data, replace with actual test data
    model.evaluate(X_test, y_test)
    
    # Save the trained model
    joblib.dump(model, 'trained_model.pkl')

    return model

if __name__ == '__main__':
    train_model()