# aqi-prediction-app
All these data only for Tashkent city.

## AQI Prediction App

### Setup and Installation

#### 1. Clone the repository
```sh
   git clone https://github.com/khurshiduktamov/aqi-prediction-app.git
   cd aqi-prediction-app
#### 2. Installing dependencies
```sh
   pip install -r requirements.txt
#### 3. Run the streamlit app
```sh
   streamlit run app/main.py

Workflow

This project uses GitHub Actions to automate data fetching, transformation, model training, and predictions.
Usage

    The workflow is triggered daily at 11 AM UTC+5.
    Predictions are saved in data/processed/predictions.csv.


#### 4. Monitoring

Set up notifications for workflow failures:

- Go to your repository settings on GitHub.
- Navigate to **Settings** > **Branches** > **Branch protection rules**.
- Set up rules and notifications for the `main` branch.

#### 5. Backup and Versioning

Ensure you have backups and proper versioning for:

- Raw and processed data.
- Trained models.

You can use Git LFS for large files:

```sh
git lfs install
git lfs track "*.pkl"
git add .gitattributes
git add data/models/prophet_model.pkl
git commit -m "Track model files with Git LFS"
git push
