import pandas as pd
import json

# Load historical data
historical_data_path = 'data/backdata/tashkent-us embassy-air-quality.csv'
historical_data = pd.read_csv(historical_data_path)
historical_data.columns = ['date', 'pm25', 'pm10', 'o3', 'so2', 'co']
historical_data = historical_data[historical_data.index < 1792]  # dropping ~20 blank rows

# Convert date to 'YYYY-MM-DD' format
historical_data['date'] = pd.to_datetime(historical_data['date'], errors='coerce').dt.strftime('%Y-%m-%d')

# Load new data from JSON file
new_data_path = 'data/raw/weather_data.json'
with open(new_data_path, 'r') as f:
    new_data_json = json.load(f)

# Extract relevant information from all entries
new_data_entries = []
if isinstance(new_data_json['data'], list) and len(new_data_json['data']) > 0:
    for entry in new_data_json['data']:
        entry_data = entry['data']
        new_data_date = entry_data['time']['s'][:10]  # Extract date in 'YYYY-MM-DD' format
        pm25_value = entry_data['iaqi']['pm25']['v']
        pm10_value = entry_data['forecast']['daily']['pm10'][0]['avg'] if 'pm10' in entry_data['forecast']['daily'] else None
        o3_value = entry_data['forecast']['daily']['o3'][0]['avg'] if 'o3' in entry_data['forecast']['daily'] else None
        so2_value = entry_data['iaqi']['so2']['v'] if 'so2' in entry_data['iaqi'] else None
        co_value = entry_data['iaqi']['co']['v'] if 'co' in entry_data['iaqi'] else None

        new_data_entries.append({
            'date': new_data_date,
            'pm25': pm25_value,
            'pm10': pm10_value,
            'o3': o3_value,
            'so2': so2_value,
            'co': co_value
        })

# Create a DataFrame for the new data
new_data_df = pd.DataFrame(new_data_entries)
new_data_df['date'] = pd.to_datetime(new_data_df['date']).dt.strftime('%Y-%m-%d')

# Combine historical data with new data
combined_data = pd.concat([historical_data, new_data_df], ignore_index=True)

# Sort by date in ascending order
combined_data = combined_data.sort_values(by='date')

# Drop duplicate rows based on 'date' column
combined_data = combined_data.drop_duplicates(subset=['date'], keep='last')

# Drop columns with all NaN values
combined_data = combined_data.drop(columns=['pm10', 'o3', 'so2', 'co'])

# Save the combined data back to CSV
combined_data_path = 'data/processed/processed_data.csv'
combined_data.to_csv(combined_data_path, index=False)

# Output the combined data to check
print(combined_data)
