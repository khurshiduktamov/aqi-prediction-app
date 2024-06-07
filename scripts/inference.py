import pandas as pd
from statsmodels.tsa.arima.model import ARIMAResults
import joblib
from datetime import datetime, timedelta

# Load the model
model_path = 'data/models/arima_model.pkl'
model_fit = joblib.load(model_path)

# Load the processed data
data_path = 'data/processed/processed_data.csv'
data = pd.read_csv(data_path)

# Ensure date column is a datetime object and set frequency
data['date'] = pd.to_datetime(data['date'])
data = data.set_index('date')
data.index = pd.DatetimeIndex(data.index)  # Ensure daily frequency

# Make predictions for the next 5 days
forecast_steps = 5
forecast = model_fit.get_forecast(steps=forecast_steps)
predicted_mean = forecast.predicted_mean

# Create a DataFrame for the forecast
start_date = data.index[-1]
dates = [start_date + timedelta(days=i) for i in range(1, forecast_steps + 1)]
forecast_df = pd.DataFrame({'date': dates, 'pm25': predicted_mean.values})

forecast_df['pm25'] = forecast_df['pm25'].astype(int)

# Save the forecast
forecast_path = 'data/processed/predictions.csv'
forecast_df.to_csv(forecast_path, index=False)

print(f"Forecast saved to {forecast_path}")
