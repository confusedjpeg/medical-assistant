import pandas as pd
import os

def get_medicine_data(medicine_name):
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'medicine_data.csv')
    try:
        data = pd.read_csv(csv_path)
        record = data[data['name'].str.lower() == medicine_name.lower()]
        return record.to_dict('records')[0] if not record.empty else None
    except Exception as e:
        print("Error loading medicine data:", e)
        return None

def get_all_medicines():
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'medicine_data.csv')
    try:
        data = pd.read_csv(csv_path)
        return data['name'].tolist()
    except Exception as e:
        print("Error loading medicine data:", e)
        return []

def get_medicine_suggestions(query):
    """
    Returns medicine names that match the query using simple substring matching.
    """
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'medicine_data.csv')
    try:
        data = pd.read_csv(csv_path)
        medicinelist = data['name'].tolist()
        suggestions = [name for name in medicinelist if query.lower() in name.lower()]
        return suggestions
    except Exception as e:
        print("Error fetching medicine suggestions:", e)
        return []