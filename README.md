# 🎓 Student Pass Prediction API

## 📌 Project Overview

This project is a **Machine Learning API** built using **FastAPI** to predict whether a student will pass or fail based on academic and lifestyle factors.

The model is trained using real-world-like data and deployed using **Docker**, making it portable and production-ready.

---

## 🚀 Tech Stack

* **Python**
* **FastAPI**
* **Scikit-learn**
* **Pandas & NumPy**
* **Docker**
* **Uvicorn**

---

## 📊 Features

* Predict student pass/fail outcome
* REST API with FastAPI
* Model trained with supervised learning
* Dockerized for easy deployment
* Ready for cloud deployment (Railway)

---

## 📁 Project Structure

```
ml-mle-students5k-rows/
│
├── app.py              # FastAPI application
├── model.joblib        # Trained ML model
├── requirements.txt    # Dependencies
├── Dockerfile          # Docker configuration
└── README.md           # Project documentation
```

---

## ▶️ How to Run (Local)

### 1. Clone Repository

```bash
git clone https://github.com/Leviathanxxz/ml-mle-student5k.git
cd ml-mle-student5k
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run API

```bash
uvicorn app:app --reload
```

### 4. Open in Browser

```
http://localhost:8000/docs
```

---

## 🐳 Run with Docker

### Build Image

```bash
docker build -t ml-api .
```

### Run Container

```bash
docker run -p 8000:8000 ml-api
```

### Access API

```
http://localhost:8000/docs
```

---

## 🌐 API Endpoints

### 🔹 GET `/`

Check API status

### 🔹 POST `/predict`

Predict student result

---

## 📥 Example Request

```json
{
  "study_hours": 6,
  "attendance": 80,
  "sleep_hours": 7,
  "previous_score": 75,
  "assignment_score": 85,
  "internet_usage": 5,
  "parent_education": 3,
  "stress_level": 4,
  "part_time_job": 0,
  "health_score": 70
}
```

---

## 📤 Example Response

```json
{
  "prediction": 1
}
```

**Note:**

* `1` = Pass
* `0` = Fail

---

## 🧠 Machine Learning Details

* Model: Logistic Regression / Pipeline
* Scaling: StandardScaler
* Hyperparameter tuning: RandomizedSearchCV
* Dataset: 5000 rows (simulated real-world student data)

---

## ☁️ Deployment

This project is ready to be deployed using:

* Railway
* Render
* Docker-based platforms

---

## 📌 Author

Developed as part of a Machine Learning Engineering learning project.

---

## ⭐ Notes

This project demonstrates:

* End-to-end ML pipeline
* API development
* Docker containerization
* Real-world deployment workflow
