### README.md for Weather Prediction App

## Weather Prediction App

This project is a comprehensive weather and air quality prediction application built using Python, Streamlit, and various data science tools. The app displays current weather conditions, air quality index (AQI), and predicts PM2.5 levels for the next five days. The project is structured to facilitate data fetching, processing, model training, and deployment in a systematic manner.

### Project Structure

```
weather-prediction-app/
├── data/
│   ├── raw/                   # Raw data from external sources
│   ├── processed/             # Processed data ready for analysis
│   ├── models/                # Trained models
│   └── backdata/              # Historical data storage
│       └── historical_data.csv
├── notebooks/
│   ├── model_training.ipynb   # Jupyter notebook for model training
├── scripts/
│   ├── fetch_weather_data.py  # Script to fetch weather data from APIs
│   ├── transform_data.py      # Script to transform raw data
│   ├── train_model.py         # Script to train predictive models
│   ├── inference.py           # Script for model inference
├── app/
│   ├── main.py                # Streamlit app script
├── .github/
│   └── workflows/
│       └── daily_fetch.yml    # GitHub Actions workflow for daily data fetch
├── requirements.txt           # Python dependencies
├── Dockerfile                 # Dockerfile for containerizing the app
├── dvc.yaml                   # DVC pipeline file
├── .gitignore                 # Git ignore file
└── README.md                  # Project documentation
```

### Steps and Detailed Explanations

#### 1. Data Collection
- **Scripts**: `fetch_weather_data.py`
- **Details**: This script fetches current weather data and AQI from external APIs. It is scheduled to run daily using GitHub Actions (`daily_fetch.yml`) to ensure the data is up-to-date.

#### 2. Data Storage
- **Directory**: `data/raw/`
- **Details**: Raw data fetched from APIs is stored in this directory. Historical data is archived in `data/backdata/historical_data.csv` for long-term storage and future analysis.

#### 3. Data Processing
- **Scripts**: `transform_data.py`
- **Details**: This script processes raw data, cleaning and transforming it into a format suitable for analysis and modeling. Processed data is stored in `data/processed/`.

#### 4. Model Training
- **Notebook**: `notebooks/model_training.ipynb`
- **Scripts**: `train_model.py`
- **Details**: The Jupyter notebook contains exploratory data analysis (EDA) and initial model training. The `train_model.py` script is used to automate model training and save the trained models in `data/models/`.

#### 5. Model Inference
- **Scripts**: `inference.py`
- **Details**: This script loads the trained model and makes predictions on new data. Predictions are stored in `data/processed/predictions.csv`.

#### 6. Streamlit App
- **Script**: `app/main.py`
- **Details**: The Streamlit app displays current weather conditions, AQI, and PM2.5 predictions. It includes various UI enhancements like icons and interactive plots for better user experience.

#### 7. Continuous Integration
- **File**: `.github/workflows/daily_fetch.yml`
- **Details**: GitHub Actions workflow to automate daily data fetching and updating the repository with new data.

#### 8. Dependency Management
- **File**: `requirements.txt`
- **Details**: Lists all Python dependencies required to run the project.

#### 9. Containerization
- **File**: `Dockerfile`
- **Details**: Dockerfile to containerize the application for deployment. It sets up the environment, installs dependencies, and runs the Streamlit app.

### Deployment
- **Details**: The app can be deployed using various platforms like Heroku, AWS, or any Docker-compatible environment. The Dockerfile facilitates easy deployment by encapsulating the app in a container.

