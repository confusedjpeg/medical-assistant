import pandas as pd
import os

def get_medicine_data(medicine_name):
    """
    Fetches medicine data from the local CSV file based on the provided medicine name.
    
    Args:
        medicine_name (str): The name of the medicine to retrieve data for.
    
    Returns:
        dict: A dictionary containing medicine data, or None if not found.
    """
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'medicine_data.csv')
    try:
        data = pd.read_csv(csv_path)
        # Assuming the column name is "name"
        record = data[data['name'].str.lower() == medicine_name.lower()]
        return record.to_dict('records')[0] if not record.empty else None
    except Exception as e:
        print("Error loading medicine data:", e)
        return None

def get_all_medicines():
    """
    Retrieves a list of all available medicines' names from the CSV file.
    
    Returns:
        list: A list of medicine names, or an empty list if no data is available.
    """
    csv_path = os.path.join(os.path.dirname(__file__), 'data', 'medicine_data.csv')
    try:
        data = pd.read_csv(csv_path)
        return data['name'].tolist()
    except Exception as e:
        print("Error loading medicine data:", e)
        return []