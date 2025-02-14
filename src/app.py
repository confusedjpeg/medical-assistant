from flask import Flask, render_template, request
from api.drug_interactions import fetch_drug_interactions
from api.medicine_data import get_medicine_data
from ml.model import predict_medicine
from dotenv import load_dotenv
import os

load_dotenv()  # Loads the variables from the .env file

secret_key = os.getenv('SECRET_KEY')
database_url = os.getenv('DATABASE_URL')
debug_mode = os.getenv('DEBUG')

print(secret_key, database_url, debug_mode)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    medicines = request.form.getlist('medicines')
    symptoms = request.form.getlist('symptoms')
    
    # Fetch drug interactions and medicine data
    interactions = fetch_drug_interactions(medicines)
    medicine_data = get_medicine_data(medicines)
    
    # Predict the recommended medicine based on symptoms
    recommended_medicine = predict_medicine(symptoms, medicine_data)
    
    return render_template('results.html', interactions=interactions, recommended_medicine=recommended_medicine)

if __name__ == '__main__':
    app.run(debug=True)