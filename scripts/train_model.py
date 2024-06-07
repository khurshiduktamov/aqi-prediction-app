# train_model.py
import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
import joblib

# Load the processed data
data_path = 'data/processed/processed_data.csv'
data = pd.read_csv(data_path)

# Prepare data
data['date'] = pd.to_datetime(data['date'])
data.set_index('date', inplace=True)

# Train ARIMA model
model = ARIMA(data['pm25'], order=(5, 1, 0))  # (p, d, q) order parameters can be tuned
model_fit = model.fit()

# Save the model
model_path = 'data/models/arima_model.pkl'
joblib.dump(model_fit, model_path)

print(f"Model trained and saved to {model_path}")
