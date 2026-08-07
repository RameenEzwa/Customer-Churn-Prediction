import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from src.predict import predict_churn
import streamlit as st
from src.predict import predict_churn

st.title("Customer Churn Prediction")

st.write("Enter customer details to predict whether the customer is likely to churn.")

#Numerical Inputs
tenure = st.number_input("Tenure (Months)", min_value=0, max_value=100, value=12)

MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=50.0)

TotalCharges = st.number_input("Total Charges", min_value=0.0, value=500.0)

# Categorical Inputs
gender = st.selectbox("Gender", ["Female", "Male"])

SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])

Partner = st.selectbox("Partner", ["No", "Yes"])

Dependents = st.selectbox("Dependents", ["No", "Yes"])

PhoneService = st.selectbox("Phone Service", ["No", "Yes"])

MultipleLines = st.selectbox("Multiple Lines", ["No", "Yes"])

InternetService = st.selectbox(
    "Internet Service",
    ["DSL", "Fiber optic", "No"]
)

OnlineSecurity = st.selectbox(
    "Online Security",
    ["No", "Yes", "No internet service"]
)

OnlineBackup = st.selectbox(
    "Online Backup",
    ["No", "Yes", "No internet service"]
)

DeviceProtection = st.selectbox(
    "Device Protection",
    ["No", "Yes", "No internet service"]
)

TechSupport = st.selectbox(
    "Tech Support",
    ["No", "Yes", "No internet service"]
)

StreamingTV = st.selectbox(
    "Streaming TV",
    ["No", "Yes", "No internet service"]
)

StreamingMovies = st.selectbox(
    "Streaming Movies",
    ["No", "Yes", "No internet service"]
)

Contract = st.selectbox(
    "Contract",
    ["Month-to-month", "One year", "Two year"]
)

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)

PaymentMethod = st.selectbox(
    "Payment Method",
    [
        "Electronic check",
        "Mailed check",
        "Bank transfer (automatic)",
        "Credit card (automatic)"
    ]
)

#Predict Butons
if st.button("Predict Churn"):

    customer_data = {
        "gender": gender,
        "SeniorCitizen": SeniorCitizen,
        "Partner": Partner,
        "Dependents": Dependents,
        "tenure": tenure,
        "PhoneService": PhoneService,
        "MultipleLines": MultipleLines,
        "InternetService": InternetService,
        "OnlineSecurity": OnlineSecurity,
        "OnlineBackup": OnlineBackup,
        "DeviceProtection": DeviceProtection,
        "TechSupport": TechSupport,
        "StreamingTV": StreamingTV,
        "StreamingMovies": StreamingMovies,
        "Contract": Contract,
        "PaperlessBilling": PaperlessBilling,
        "PaymentMethod": PaymentMethod,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "IsSenior": SeniorCitizen,
    }

    result = predict_churn(customer_data)

    if "likely" in result.lower():
        st.error("⚠️ Prediction: Customer is likely to churn.")
        st.warning("Recommendation: Offer discounts or loyalty plans to retain the customer.")
    else:
        st.success("✅ Prediction: Customer is not likely to churn.")
        st.info("The customer is expected to remain with the company.")
