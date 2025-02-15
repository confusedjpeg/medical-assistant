from flask import Flask, render_template, request, jsonify
from src.api.medicine_data import get_medicine_data, get_all_medicines, get_medicine_suggestions
from src.ml.model import MedicalAssistantModel
from src.database import Database
from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()  # Loads the variables from the .env file

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(
            database=os.getenv('DB_NAME'),
            user=os.getenv('DB_USER'),
            password=os.getenv('DB_PASSWORD'),
            host=os.getenv('DB_HOST'),
            port=os.getenv('DB_PORT')
        )
        self.conn.autocommit = True
        self.create_inventory_table()

    def create_inventory_table(self):
        self.execute_query("""
        CREATE TABLE IF NOT EXISTS inventory (
            id SERIAL PRIMARY KEY,
            medicine_name VARCHAR(255) NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
        """)

    def execute_query(self, query, params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)

    def fetch_all(self, query, params=None):
        with self.conn.cursor() as cursor:
            cursor.execute(query, params)
            return cursor.fetchall()

# Ensure you have a global db instance created at the top of the file.
db = Database()

# In-memory storage for user inventory (for simplicity)
user_inventory = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/add_medicine', methods=['POST'])
def add_medicine():
    medicine_name = request.json['medicine_name']
    # Insert the medicine into the inventory table
    db.execute_query("INSERT INTO inventory (medicine_name) VALUES (%s)", (medicine_name,))
    # Query all inventory entries
    rows = db.fetch_all("SELECT medicine_name FROM inventory")
    inventory = [row[0] for row in rows]
    return jsonify({'status': 'success', 'inventory': inventory})

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.json['symptoms']
    model = MedicalAssistantModel()
    predicted_medicines, medicine_details, interactions = model.predict([symptoms])
    inventory_predictions = [med for med in predicted_medicines if med in user_inventory]
    return jsonify({
        'predicted_medicines': inventory_predictions,
        'medicine_details': medicine_details,
        'interactions': interactions
    })

@app.route('/autocomplete', methods=['GET'])
def autocomplete():
    query = request.args.get('query', '')
    suggestions = get_medicine_suggestions(query) if query else []
    return jsonify({'suggestions': suggestions})

if __name__ == '__main__':
    app.run(debug=True)