import streamlit as st
import numpy as np
import joblib
from tensorflow.keras.models import load_model

# Load model and scaler
model = load_model('ann_model.h5')
scaler = joblib.load('scaler.pkl')

st.title("🏦 Customer Churn Predictor")

# Input fields
credit_score = st.number_input("Credit Score", 300, 900, 600)
gender = st.selectbox("Gender", ['Male', 'Female'])
age = st.number_input("Age", 18, 100, 40)
tenure = st.number_input("Tenure (Years)", 0, 10, 3)
balance = st.number_input("Balance", 0.0, 300000.0, 60000.0)
products = st.selectbox("Number of Products", [1, 2, 3, 4])
has_card = st.selectbox("Has Credit Card", [1, 0])
is_active = st.selectbox("Is Active Member", [1, 0])
salary = st.number_input("Estimated Salary", 0.0, 300000.0, 50000.0)
geo = st.selectbox("Geography", ['France', 'Germany', 'Spain'])

# Encode gender and geography
gender = 1 if gender == 'Male' else 0
geo_encoded = [1, 0, 0] if geo == 'France' else [0, 1, 0] if geo == 'Germany' else [0, 0, 1]

# Create final input array
input_data = np.array([[*geo_encoded, credit_score, gender, age, tenure,
                        balance, products, has_card, is_active, salary]])
input_scaled = scaler.transform(input_data)

if st.button("Predict Churn"):
    pred = model.predict(input_scaled)
    st.success("🚫 Customer will NOT churn" if pred <= 0.5 else "⚠️ Customer is LIKELY to churn")
