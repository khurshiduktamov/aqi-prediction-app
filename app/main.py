import streamlit as st
import pandas as pd
import json
import plotly.express as px

# Set the page title
st.set_page_config(page_title="AQI Predictions")

# Add GitHub link with logo at the top
st.markdown(
    """
    <div style="display: flex; align-items: center;">
        <h3><a href="https://github.com/khurshiduktamov/aqi-prediction-app" target="_blank">
            <img src="https://img.icons8.com/ios-filled/50/007BFF/github.png" alt="GitHub" style="margin-right: 10px;">Github Repository   
        </a>
        </h3>
    </div>
    """,
    unsafe_allow_html=True
)


# Load predictions
predictions_path = 'data/processed/predictions.csv'
predictions = pd.read_csv(predictions_path)

# Load weather data
weather_data_path = 'data/raw/weather_data.json'
with open(weather_data_path) as f:
    weather_data = json.load(f)

# Extract the most recent weather details
latest_weather_entry = weather_data['data'][-1]['data']
aqi = latest_weather_entry['aqi']

# Safely get weather metrics with fallback values
def get_iaqi_value(iaqi_dict, key, default_value=0):
    try:
        return iaqi_dict[key]['v']
    except (KeyError, TypeError):
        return default_value

temp = get_iaqi_value(latest_weather_entry['iaqi'], 't')
humidity = get_iaqi_value(latest_weather_entry['iaqi'], 'h')
pressure = get_iaqi_value(latest_weather_entry['iaqi'], 'p')
wind_speed = get_iaqi_value(latest_weather_entry['iaqi'], 'w')
wind_gust = get_iaqi_value(latest_weather_entry['iaqi'], 'wg')
dew_point = get_iaqi_value(latest_weather_entry['iaqi'], 'dew')
city_name = latest_weather_entry['city']['name']
update_time = latest_weather_entry['time']['iso']

# Streamlit app
st.title('Air Quality Prediction App')

# Display current weather
st.header(f"Current Weather in {city_name}")
st.write(f"Last updated: {update_time}")

# Display weather metrics in columns with icons
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("AQI", aqi, help="Air Quality Index")
    st.image("https://img.icons8.com/color/48/000000/air-quality.png", width=30)
with col2:
    st.metric("Temperature (°C)", temp)
    st.image("https://img.icons8.com/color/48/000000/temperature.png", width=30)
with col3:
    st.metric("Humidity (%)", humidity)
    st.image("https://img.icons8.com/color/48/000000/humidity.png", width=30)

col4, col5, col6 = st.columns(3)
with col4:
    st.metric("Pressure (hPa)", pressure)
    st.image("https://img.icons8.com/color/48/000000/pressure.png", width=30)
with col5:
    st.metric("Wind Speed (m/s)", wind_speed)
    st.image("https://img.icons8.com/color/48/000000/wind.png", width=30)
with col6:
    st.metric("Wind Gust (m/s)", wind_gust)
    st.image("https://cdn-icons-png.flaticon.com/512/740/740832.png", width=30)

col7, _ = st.columns(2)
with col7:
    st.metric("Dew Point (°C)", dew_point)
    st.image("https://img.icons8.com/color/48/000000/dew-point.png", width=30)

# Display PM2.5 predictions
st.header('PM2.5 Predictions for the Next 5 Days')
st.write(predictions)

# Plot predictions with Plotly for better visuals
fig = px.line(predictions, x='date', y='pm25', title='PM2.5 Predictions', labels={'date': 'Date', 'pm25': 'PM2.5 Level'})
fig.update_layout(title_x=0.5, title_font=dict(size=24), xaxis_title_font=dict(size=18), yaxis_title_font=dict(size=18))
st.plotly_chart(fig)

# Add AQI information table
st.header('Air Quality Index (AQI) Information')
aqi_info = {
    "AQI": ["0 - 50", "51 - 100", "101 - 150", "151 - 200", "201 - 300", "300+"],
    "Air Pollution Level": ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"],
    "Health Implications": [
        "Air quality is considered satisfactory, and air pollution poses little or no risk.",
        "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.",
        "Members of sensitive groups may experience health effects. The general public is not likely to be affected.",
        "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.",
        "Health warnings of emergency conditions. The entire population is more likely to be affected.",
        "Health alert: everyone may experience more serious health effects."
    ],
    "Cautionary Statement (for PM2.5)": [
        "None",
        "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion.",
        "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion.",
        "Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion.",
        "Active children and adults, and people with respiratory disease, such as asthma, should avoid all outdoor exertion; everyone else, especially children, should limit outdoor exertion.",
        "Everyone should avoid all outdoor exertion."
    ]
}

# Create a DataFrame for AQI information
aqi_df = pd.DataFrame(aqi_info)

# Define colors based on AQI levels
colors = {
    "Good": "#009966",
    "Moderate": "#FFDE33",
    "Unhealthy for Sensitive Groups": "#FF9933",
    "Unhealthy": "#CC0033",
    "Very Unhealthy": "#660099",
    "Hazardous": "#7E0023"
}

# Apply colors to the AQI levels
def color_row(row):
    return [f'background-color: {colors[row["Air Pollution Level"]]}']*len(row)

st.dataframe(aqi_df.style.apply(color_row, axis=1))

# Show a map of the city location
st.map(pd.DataFrame([[latest_weather_entry['city']['geo'][0], latest_weather_entry['city']['geo'][1]]], columns=['lat', 'lon']))

# Adding footer for attributions
st.write("### Data Attributions")
for attribution in latest_weather_entry['attributions']:
    st.markdown(f"[{attribution['name']}]({attribution['url']})")






# old version 

# import streamlit as st
# import pandas as pd
# import json
# import plotly.express as px

# # Set the page title
# st.set_page_config(page_title="AQI Predictions")

# # Add GitHub link with logo at the top
# st.markdown(
#     """
#     <div style="display: flex; align-items: center;">
#         <h3><a href="https://github.com/khurshiduktamov/aqi-prediction-app" target="_blank">
#             <img src="https://img.icons8.com/ios-filled/50/007BFF/github.png" alt="GitHub" style="margin-right: 10px;">Github Repository   
#         </a>
#         </h3>
#     </div>
#     """,
#     unsafe_allow_html=True
# )


# # Load predictions
# predictions_path = 'data/processed/predictions.csv'
# predictions = pd.read_csv(predictions_path)

# # Load weather data
# weather_data_path = 'data/raw/weather_data.json'
# with open(weather_data_path) as f:
#     weather_data = json.load(f)

# # Extract the most recent weather details
# latest_weather_entry = weather_data['data'][-1]['data']
# aqi = latest_weather_entry['aqi']
# temp = latest_weather_entry['iaqi']['t']['v']
# humidity = latest_weather_entry['iaqi']['h']['v']
# pressure = latest_weather_entry['iaqi']['p']['v']
# wind_speed = latest_weather_entry['iaqi']['w']['v']
# wind_gust = latest_weather_entry['iaqi']['wg']['v']
# dew_point = latest_weather_entry['iaqi']['dew']['v']
# city_name = latest_weather_entry['city']['name']
# update_time = latest_weather_entry['time']['iso']

# # Streamlit app
# st.title('Air Quality Prediction App')

# # Display current weather
# st.header(f"Current Weather in {city_name}")
# st.write(f"Last updated: {update_time}")

# # Display weather metrics in columns with icons
# col1, col2, col3 = st.columns(3)
# with col1:
#     st.metric("AQI", aqi, help="Air Quality Index")
#     st.image("https://img.icons8.com/color/48/000000/air-quality.png", width=30)
# with col2:
#     st.metric("Temperature (°C)", temp)
#     st.image("https://img.icons8.com/color/48/000000/temperature.png", width=30)
# with col3:
#     st.metric("Humidity (%)", humidity)
#     st.image("https://img.icons8.com/color/48/000000/humidity.png", width=30)

# col4, col5, col6 = st.columns(3)
# with col4:
#     st.metric("Pressure (hPa)", pressure)
#     st.image("https://img.icons8.com/color/48/000000/pressure.png", width=30)
# with col5:
#     st.metric("Wind Speed (m/s)", wind_speed)
#     st.image("https://img.icons8.com/color/48/000000/wind.png", width=30)
# with col6:
#     st.metric("Wind Gust (m/s)", wind_gust)
#     st.image("https://cdn-icons-png.flaticon.com/512/740/740832.png", width=30)

# col7, _ = st.columns(2)
# with col7:
#     st.metric("Dew Point (°C)", dew_point)
#     st.image("https://img.icons8.com/color/48/000000/dew-point.png", width=30)

# # Display PM2.5 predictions
# st.header('PM2.5 Predictions for the Next 5 Days')
# st.write(predictions)

# # Plot predictions with Plotly for better visuals
# fig = px.line(predictions, x='date', y='pm25', title='PM2.5 Predictions', labels={'date': 'Date', 'pm25': 'PM2.5 Level'})
# fig.update_layout(title_x=0.5, title_font=dict(size=24), xaxis_title_font=dict(size=18), yaxis_title_font=dict(size=18))
# st.plotly_chart(fig)

# # Add AQI information table
# st.header('Air Quality Index (AQI) Information')
# aqi_info = {
#     "AQI": ["0 - 50", "51 - 100", "101 - 150", "151 - 200", "201 - 300", "300+"],
#     "Air Pollution Level": ["Good", "Moderate", "Unhealthy for Sensitive Groups", "Unhealthy", "Very Unhealthy", "Hazardous"],
#     "Health Implications": [
#         "Air quality is considered satisfactory, and air pollution poses little or no risk.",
#         "Air quality is acceptable; however, for some pollutants there may be a moderate health concern for a very small number of people who are unusually sensitive to air pollution.",
#         "Members of sensitive groups may experience health effects. The general public is not likely to be affected.",
#         "Everyone may begin to experience health effects; members of sensitive groups may experience more serious health effects.",
#         "Health warnings of emergency conditions. The entire population is more likely to be affected.",
#         "Health alert: everyone may experience more serious health effects."
#     ],
#     "Cautionary Statement (for PM2.5)": [
#         "None",
#         "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion.",
#         "Active children and adults, and people with respiratory disease, such as asthma, should limit prolonged outdoor exertion.",
#         "Active children and adults, and people with respiratory disease, such as asthma, should avoid prolonged outdoor exertion; everyone else, especially children, should limit prolonged outdoor exertion.",
#         "Active children and adults, and people with respiratory disease, such as asthma, should avoid all outdoor exertion; everyone else, especially children, should limit outdoor exertion.",
#         "Everyone should avoid all outdoor exertion."
#     ]
# }

# # Create a DataFrame for AQI information
# aqi_df = pd.DataFrame(aqi_info)

# # Define colors based on AQI levels
# colors = {
#     "Good": "#009966",
#     "Moderate": "#FFDE33",
#     "Unhealthy for Sensitive Groups": "#FF9933",
#     "Unhealthy": "#CC0033",
#     "Very Unhealthy": "#660099",
#     "Hazardous": "#7E0023"
# }

# # Apply colors to the AQI levels
# def color_row(row):
#     return [f'background-color: {colors[row["Air Pollution Level"]]}']*len(row)

# st.dataframe(aqi_df.style.apply(color_row, axis=1))


# # Show a map of the city location
# st.map(pd.DataFrame([[latest_weather_entry['city']['geo'][0], latest_weather_entry['city']['geo'][1]]], columns=['lat', 'lon']))


# # Adding footer for attributions
# st.write("### Data Attributions")
# for attribution in latest_weather_entry['attributions']:
#     st.markdown(f"[{attribution['name']}]({attribution['url']})")
