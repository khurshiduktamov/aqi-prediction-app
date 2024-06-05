import requests
import json
import os

def fetch_weather_data():
    api_endpoint = "https://api.waqi.info/feed/@11219/?token=affc18eae1eaf67d9ba5d18a1ad6752c142b09bd"
    response = requests.get(api_endpoint)
    new_data = response.json()

    file_path = "data/raw/weather_data.json"

    # Create directory if it doesn't exist
    os.makedirs(os.path.dirname(file_path), exist_ok=True)

    # Read existing data from the file if it exists
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            try:
                existing_data = json.load(f)
            except json.JSONDecodeError:
                existing_data = {'data': []}
    else:
        existing_data = {'data': []}

    # Ensure 'data' key exists and is a list
    if not isinstance(existing_data.get('data'), list):
        existing_data['data'] = []

    # Append new data to 'data' list
    existing_data['data'].append(new_data)

    # Save updated data to JSON file
    with open(file_path, "w") as f:
        json.dump(existing_data, f, indent=4)

if __name__ == "__main__":
    fetch_weather_data()
