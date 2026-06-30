import streamlit as st
import numpy as np
import joblib

# ------------------------
# Page Config
# ------------------------
st.set_page_config(
    page_title="Diabetes Prediction",
    page_icon="🩺",
    layout="wide"
)

# ------------------------
# Load Model
# ------------------------
model = joblib.load("diabetes_knn_model.pkl")

# ------------------------
# Title
# ------------------------
st.title("🩺 Diabetes Prediction")


st.write("Enter the patient's medical details below.")

# ------------------------
# Input Fields
# ------------------------

col1, col2 = st.columns(2)

with col1:

    pregnancies = st.number_input("Pregnancies",0,20,1)

    glucose = st.number_input("Glucose",0,250,120)

    blood_pressure = st.number_input("Blood Pressure",0,150,70)

    skin_thickness = st.number_input("Skin Thickness",0,100,20)

with col2:

    insulin = st.number_input("Insulin",0,900,80)

    bmi = st.number_input("BMI",0.0,70.0,25.0)

    pedigree = st.number_input(
        "Diabetes Pedigree Function",
        0.0,
        3.0,
        0.50
    )

    age = st.number_input("Age",1,120,30)

# ------------------------
# Prediction
# ------------------------

if st.button("Predict"):

    data = np.array([[
        pregnancies,
        glucose,
        blood_pressure,
        skin_thickness,
        insulin,
        bmi,
        pedigree,
        age
    ]])

    prediction = model.predict(data)[0]

    probability = model.predict_proba(data)

    if prediction == 1:
        st.error("High Risk of Diabetes")
        st.write(f"Probability : {probability[0][1]*100:.2f}%")

    else:
        st.success("No Diabetes Detected")
        st.write(f"Probability : {probability[0][0]*100:.2f}%")