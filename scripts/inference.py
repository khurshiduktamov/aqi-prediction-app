import pandas as pd
import joblib
from prophet import Prophet

# Load the processed data
data_path = 'data/processed/processed_data.csv'
data = pd.read_csv(data_path)

# Prepare data for Prophet
data = data.rename(columns={'date': 'ds', 'pm25': 'y'})

# Load the model
model_path = 'data/models/prophet_model.pkl'
model = joblib.load(model_path)

# Make future dataframe for the next 5 days
future = model.make_future_dataframe(periods=5)

# Make predictions
forecast = model.predict(future)

# Extract relevant columns
predictions = forecast[['ds', 'yhat']].tail(5)
predictions = predictions.rename(columns={'ds': 'date', 'yhat': 'predicted_pm25'})

predictions['predicted_pm25'] = predictions['predicted_pm25'].astype(int)

# Save predictions
predictions_path = 'data/processed/predictions.csv'
predictions.to_csv(predictions_path, index=False)

print(f"Predictions saved to {predictions_path}")
