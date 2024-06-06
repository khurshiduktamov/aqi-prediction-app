import pandas as pd
from prophet import Prophet
import joblib

# Load the processed data
data_path = 'data/processed/processed_data.csv'
data = pd.read_csv(data_path)

# Prepare data for Prophet
data = data.rename(columns={'date': 'ds', 'pm25': 'y'})
data['ds'] = pd.to_datetime(data['ds'])  # Ensure 'ds' is datetime

# Train-test split
train_data = data[:-30]  # Use all data except the last 30 days for training
test_data = data[-30:]   # Use the last 30 days for testing

# Initialize and train the model
model = Prophet()
model.fit(train_data)


# Make predictions
future = model.make_future_dataframe(periods=30)
forecast = model.predict(future)

# Extract predictions for the test period
predicted_test_data = forecast[['ds', 'yhat']].tail(30)

# Ensure 'ds' columns are datetime
test_data['ds'] = pd.to_datetime(test_data['ds'])
predicted_test_data['ds'] = pd.to_datetime(predicted_test_data['ds'])

# Merge actual and predicted data
test_data = test_data.rename(columns={'y': 'actual'})
merged_data = pd.merge(test_data, predicted_test_data, on='ds')


# Save the model
model_path = 'data/models/prophet_model.pkl'
joblib.dump(model, model_path)

print(f"Model trained and saved to {model_path}")
