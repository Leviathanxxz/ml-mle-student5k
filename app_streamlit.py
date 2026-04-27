import streamlit as st
import requests

st.title("🎓 Student Pass Prediction")

with st.form("form"):
    col1, col2 = st.columns(2)

    with col1:
        study_hours = st.number_input("Study Hours", 0.0, 12.0, 6.0)
        attendance = st.number_input("Attendance", 0.0, 100.0, 80.0)
        sleep_hours = st.number_input("Sleep Hours", 0.0, 12.0, 7.0)
        previous_score = st.number_input("Previous Score", 0.0, 100.0, 75.0)
        assignment_score = st.number_input("Assignment Score", 0.0, 100.0, 85.0)

    with col2:
        internet_usage = st.number_input("Internet Usage", 0.0, 10.0, 5.0)
        parent_education = st.number_input("Parent Education", 1, 5, 3)
        stress_level = st.number_input("Stress Level", 1.0, 10.0, 4.0)
        part_time_job = st.selectbox("Part Time Job", [0, 1])
        health_score = st.number_input("Health Score", 0.0, 100.0, 70.0)

    # PENTING: ini harus di dalam form
    submit = st.form_submit_button("Predict")


if submit:
    url = "https://ml-mle-student5k-production.up.railway.app/predict"

    data = {
        "study_hours": study_hours,
        "attendance": attendance,
        "sleep_hours": sleep_hours,
        "previous_score": previous_score,
        "assignment_score": assignment_score,
        "internet_usage": internet_usage,
        "parent_education": parent_education,
        "stress_level": stress_level,
        "part_time_job": part_time_job,
        "health_score": health_score
    }

    try:
        response = requests.post(url, json=data, timeout=10)

        if response.status_code == 200:
            result = response.json()["prediction"]

            if result == 1:
                st.success("🎉 LULUS")
            else:
                st.error("❌ TIDAK LULUS")
        else:
            st.error(f"API Error: {response.status_code}")

    except:
        st.error("Tidak bisa connect ke API")