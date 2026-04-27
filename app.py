from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from feature_enggineer import feature_engineering
import pandas as pd

# 1. buat API
app = FastAPI()

# 2. load model
model = joblib.load("model.joblib")

# 3. format input
class InputData(BaseModel):
    study_hours: float
    attendance: float
    sleep_hours: float
    previous_score: float
    assignment_score: float
    internet_usage: float
    parent_education: int
    stress_level: float
    part_time_job: int
    health_score: float

# 4. endpoint home
@app.get("/")
def home():
    return {"message": "================ API RUNNING ==================!"}

# 5. endpoint prediksi
@app.post("/predict")
def predict(data: InputData):
    df = pd.DataFrame([data.dict()])

    prediction = model.predict(df)

    return {"prediction": int(prediction[0])}