# Student Performance Prediction (End-to-End ML Project)

## Overview

This project is an end-to-end Machine Learning system to predict whether a student will pass or fail based on behavioral and academic features.

The system is deployed as a full-stack AI application:

* Backend API using FastAPI
* Model served via Docker
* Deployment on Railway
* Frontend interface built with Streamlit

---

## Live Demo

* Frontend: https://ml-mle-student5k-75cubcenx37phqmsfxwwx8.streamlit.app/
* API: https://ml-mle-student5k-production.up.railway.app/docs

---

## Problem Statement

Educational institutions need early prediction systems to identify students at risk of failing, allowing timely intervention.

---

## Features

* Predict student pass/fail outcome
* Probability-based risk scoring
* Interactive UI for user input
* Prediction history tracking
* Data visualization (trend analysis)

---

## Tech Stack

* Python
* Scikit-learn
* FastAPI
* Docker
* Railway
* Streamlit

---

## Machine Learning Pipeline

1. Data Cleaning
2. Feature Engineering:

   * Study/Sleep ratio
   * Attendance × Study interaction
3. Train/Test Split
4. Model Training (Logistic Regression + Hyperparameter tuning)
5. Model Evaluation
6. Model Deployment

---

## How to Run Locally

### Backend

pip install -r requirements.txt
uvicorn app:app --reload

### Frontend

streamlit run app_streamlit.py

---

## Key Highlights

* Built complete ML pipeline from scratch
* Deployed real API for prediction
* Integrated frontend and backend
* Applied feature engineering and model tuning
* Implemented user interaction and analytics

---

## Author

Agung Hidayat
