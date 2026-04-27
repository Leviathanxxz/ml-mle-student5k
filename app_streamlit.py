# import streamlit as st
# import requests

# # ===== CONFIG =====
# st.set_page_config(
#     page_title="Student Pass Predictor",
#     page_icon="🎓",
#     layout="centered"
# )

# # ===== HEADER =====
# st.title("🎓 Student Pass Prediction")
# st.markdown("Prediksi kelulusan siswa menggunakan Machine Learning")

# # ===== CARD STYLE (CSS ringan) =====
# st.markdown("""
# <style>
# .block-container {
#     padding-top: 2rem;
# }
# .stButton>button {
#     width: 100%;
#     border-radius: 10px;
#     height: 3em;
#     font-size: 16px;
# }
# </style>
# """, unsafe_allow_html=True)

# # ===== FORM =====
# with st.form("form"):
#     st.subheader("📥 Input Data Siswa")

#     col1, col2 = st.columns(2)

#     with col1:
#         study_hours = st.number_input("Study Hours", 0.0, 12.0, 6.0)
#         attendance = st.number_input("Attendance (%)", 0.0, 100.0, 80.0)
#         sleep_hours = st.number_input("Sleep Hours", 0.0, 12.0, 7.0)
#         previous_score = st.number_input("Previous Score", 0.0, 100.0, 75.0)
#         assignment_score = st.number_input("Assignment Score", 0.0, 100.0, 85.0)

#     with col2:
#         internet_usage = st.number_input("Internet Usage (hrs)", 0.0, 10.0, 5.0)
#         parent_education = st.slider("Parent Education", 1, 5, 3)
#         stress_level = st.slider("Stress Level", 1.0, 10.0, 4.0)
#         part_time_job = st.selectbox("Part Time Job", ["No", "Yes"])
#         health_score = st.number_input("Health Score", 0.0, 100.0, 70.0)

#     submit = st.form_submit_button("🚀 Predict")

# # ===== PROCESS =====
# if submit:

#     if sleep_hours == 0:
#         st.warning("Sleep hours tidak boleh 0")
#     else:
#         url = "https://ml-mle-student5k-production.up.railway.app/predict"

#         data = {
#             "study_hours": study_hours,
#             "attendance": attendance,
#             "sleep_hours": sleep_hours,
#             "previous_score": previous_score,
#             "assignment_score": assignment_score,
#             "internet_usage": internet_usage,
#             "parent_education": parent_education,
#             "stress_level": stress_level,
#             "part_time_job": 1 if part_time_job == "Yes" else 0,
#             "health_score": health_score
#         }

#         try:
#             with st.spinner("🔍 Menganalisis data..."):
#                 response = requests.post(url, json=data, timeout=10)

#             if response.status_code == 200:
#                 result = response.json()["prediction"]
#                 prob = response.json().get("probability", 0)

#                 st.divider()
#                 st.subheader("📊 Hasil Prediksi")

#                 # RESULT BOX
#                 if result == 1:
#                     st.success("🎉 LULUS")
#                 else:
#                     st.error("❌ TIDAK LULUS")

#                 # PROBABILITY
#                 st.write(f"Confidence: **{prob*100:.2f}%**")
#                 st.progress(prob)

#             else:
#                 st.error(f"API Error: {response.status_code}")

#         except Exception as e:
#             st.error(f"Error: {e}")

import streamlit as st
import requests
import pandas as pd
from datetime import datetime

# ================= CONFIG =================
st.set_page_config(
    page_title="Student Performance AI",
    layout="wide"
)

# ================= CSS =================
st.markdown("""
<style>
.main {
    background: linear-gradient(135deg, #0f172a, #020617);
}

h1, h2, h3 {
    color: #e2e8f0;
}

.card {
    background: #111827;
    padding: 20px;
    border-radius: 16px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.3);
    margin-bottom: 15px;
}

.stButton > button {
    background: linear-gradient(90deg, #22c55e, #16a34a);
    color: white;
    border-radius: 12px;
    height: 3em;
    font-weight: bold;
    border: none;
}

.stButton > button:hover {
    background: linear-gradient(90deg, #16a34a, #15803d);
}

section[data-testid="stSidebar"] {
    background-color: #020617;
}

[data-testid="metric-container"] {
    background: #111827;
    border-radius: 12px;
    padding: 10px;
}
</style>
""", unsafe_allow_html=True)

# ================= SESSION =================
if "history" not in st.session_state:
    st.session_state.history = []

# ================= SIDEBAR =================
st.sidebar.title("Pengaturan")

api_url = st.sidebar.text_input(
    "Endpoint API",
    value="https://ml-mle-student5k-production.up.railway.app/predict"
)

show_table = st.sidebar.toggle("Tampilkan Riwayat", True)

st.sidebar.markdown("---")
st.sidebar.write("Model: Logistic Regression")

# ================= HEADER =================
st.title("Prediksi Kelulusan Siswa")

st.markdown("### Sistem Prediksi Berbasis Machine Learning")
st.markdown(
    "<span style='color:#94a3b8'>FastAPI • Docker • Railway • Streamlit</span>",
    unsafe_allow_html=True
)

# ================= LAYOUT =================
col1, col2 = st.columns([1, 1.2])

# ================= INPUT =================
with col1:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Input Data")

    study_hours = st.slider("Jam Belajar", 0.0, 12.0, 6.0)
    attendance = st.slider("Kehadiran (%)", 0.0, 100.0, 80.0)
    sleep_hours = st.slider("Jam Tidur", 0.0, 12.0, 7.0)
    previous_score = st.slider("Nilai Sebelumnya", 0.0, 100.0, 75.0)
    assignment_score = st.slider("Nilai Tugas", 0.0, 100.0, 85.0)

    internet_usage = st.slider("Penggunaan Internet", 0.0, 10.0, 5.0)
    parent_education = st.slider("Pendidikan Orang Tua", 1, 5, 3)
    stress_level = st.slider("Tingkat Stres", 1.0, 10.0, 4.0)
    part_time_job = st.selectbox("Pekerjaan Part Time", ["Tidak", "Ya"])
    health_score = st.slider("Kesehatan", 0.0, 100.0, 70.0)

    predict_btn = st.button("Prediksi")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= OUTPUT =================
with col2:
    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Hasil Prediksi")

    if not st.session_state.history:
        st.info("Belum ada prediksi")

    st.markdown('</div>', unsafe_allow_html=True)

# ================= PREDICTION =================
if predict_btn:

    if sleep_hours == 0:
        st.warning("Jam tidur tidak boleh nol")
    else:
        payload = {
            "study_hours": study_hours,
            "attendance": attendance,
            "sleep_hours": sleep_hours,
            "previous_score": previous_score,
            "assignment_score": assignment_score,
            "internet_usage": internet_usage,
            "parent_education": parent_education,
            "stress_level": stress_level,
            "part_time_job": 1 if part_time_job == "Ya" else 0,
            "health_score": health_score
        }

        try:
            with st.spinner("Memproses..."):
                res = requests.post(api_url, json=payload, timeout=10)

            if res.status_code == 200:
                data = res.json()

                pred = int(data["prediction"])
                prob = float(data.get("probability", 0))

                m1, m2, m3 = st.columns(3)

                m1.metric("Probabilitas", f"{prob*100:.2f}%")

                if prob > 0.7:
                    m2.metric("Risiko", "Rendah")
                elif prob > 0.4:
                    m2.metric("Risiko", "Sedang")
                else:
                    m2.metric("Risiko", "Tinggi")

                m3.metric("Keputusan", "Lulus" if pred == 1 else "Tidak")

                st.progress(prob)

                if pred == 1:
                    st.success("Diprediksi Lulus")
                else:
                    st.error("Berisiko Tidak Lulus")

                st.subheader("Insight")

                if prob > 0.7:
                    st.info("Performa sangat baik")
                elif prob > 0.4:
                    st.warning("Perlu peningkatan")
                else:
                    st.error("Perlu perhatian serius")

                # simpan history
                st.session_state.history.append({
                    "waktu": datetime.now().strftime("%H:%M:%S"),
                    "hasil": "Lulus" if pred == 1 else "Tidak",
                    "probabilitas": prob
                })

            else:
                st.error(f"Error API: {res.status_code}")

        except Exception as e:
            st.error(str(e))

# ================= HISTORY =================
st.markdown("---")
st.subheader("Riwayat")

if st.session_state.history:
    df = pd.DataFrame(st.session_state.history)

    if show_table:
        st.dataframe(df, use_container_width=True)

    st.line_chart(df["probabilitas"])

    csv = df.to_csv(index=False).encode("utf-8")
    st.download_button(
        "Download CSV",
        csv,
        "history_prediksi.csv",
        "text/csv"
    )

    if st.button("Hapus Riwayat"):
        st.session_state.history = []
        st.rerun()
else:
    st.info("Belum ada data")