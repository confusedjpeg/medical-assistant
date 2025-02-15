from flask import Flask, render_template, request, jsonify
from src.api.drug_interactions import DrugInteractionChecker
from src.api.medicine_data import get_medicine_data, get_all_medicines
from src.ml.model import MedicalAssistantModel
from dotenv import load_dotenv
import os

load_dotenv()  # Loads the variables from the .env file

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

# In-memory storage for user inventory (for simplicity)
user_inventory = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_medicine', methods=['POST'])
def add_medicine():
    medicine_name = request.json['medicine_name']
    user_inventory.append(medicine_name)
    return jsonify({'status': 'success', 'inventory': user_inventory})

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.json['symptoms']
    model = MedicalAssistantModel()
    predicted_medicines, medicine_details, interactions = model.predict([symptoms])
    
    # Filter predictions based on user inventory
    inventory_predictions = [med for med in predicted_medicines if med in user_inventory]
    
    return jsonify({
        'predicted_medicines': inventory_predictions,
        'medicine_details': medicine_details,
        'interactions': interactions
    })

if __name__ == '__main__':
    app.run(debug=True)