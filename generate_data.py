import pandas as pd
import numpy as np

np.random.seed(42)
n = 5000

study_hours = np.random.normal(6, 2, n).clip(0, 12)
attendance = np.random.normal(80, 10, n).clip(50, 100)
sleep_hours = np.random.normal(7, 1.5, n).clip(3, 10)

previous_score = (study_hours * 5 + np.random.normal(50, 10, n)).clip(0, 100)
assignment_score = (study_hours * 6 + np.random.normal(40, 10, n)).clip(0, 100)

internet_usage = np.random.normal(5, 2, n).clip(1, 10)
parent_education = np.random.randint(1, 5, n)
stress_level = np.random.normal(5, 2, n).clip(1, 10)
part_time_job = np.random.randint(0, 2, n)
health_score = np.random.normal(70, 15, n).clip(30, 100)

score = (
    0.3 * study_hours +
    0.2 * attendance +
    0.2 * previous_score +
    0.15 * assignment_score -
    0.2 * stress_level -
    0.1 * internet_usage +
    0.1 * health_score
)

prob = 1 / (1 + np.exp(-0.05 * (score - 50)))
lulus = (prob > 0.5).astype(int)

df = pd.DataFrame({
    "study_hours": study_hours,
    "attendance": attendance,
    "sleep_hours": sleep_hours,
    "previous_score": previous_score,
    "assignment_score": assignment_score,
    "internet_usage": internet_usage,
    "parent_education": parent_education,
    "stress_level": stress_level,
    "part_time_job": part_time_job,
    "health_score": health_score,
    "lulus": lulus
})

df.to_csv("data.csv", index=False)

print("Dataset berhasil dibuat!")