import streamlit as st
import pandas as pd

# Load predictions
predictions_path = 'data/processed/predictions.csv'
predictions = pd.read_csv(predictions_path)

# Streamlit app
st.title('Weather Prediction App')

st.write('## PM2.5 Predictions for the Next 5 Days')
st.write(predictions)

# Plot predictions
st.line_chart(predictions.set_index('date')['predicted_pm25'])
