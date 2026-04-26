from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

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
    study_sleep_ratio: float
    attendance_study_interaction: float

# 4. endpoint home
@app.get("/")
def home():
    return {"message": "API running!"}

# 5. endpoint prediksi
@app.post("/predict")
def predict(data: InputData):

    features = np.array([[
        data.study_hours,
        data.attendance,
        data.sleep_hours,
        data.previous_score,
        data.assignment_score,
        data.internet_usage,
        data.parent_education,
        data.stress_level,
        data.part_time_job,
        data.health_score,
        data.study_sleep_ratio,
        data.attendance_study_interaction
    ]])

    prediction = model.predict(features)

    return {"prediction": int(prediction[0])}