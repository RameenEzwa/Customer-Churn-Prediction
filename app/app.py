import sys
import os

sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

import streamlit as st
from src.predict import predict_churn


# ---------------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------------
st.set_page_config(
    page_title="Customer Churn Prediction",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------------
st.markdown("""
<style>

    /* Main background */
    .stApp {
        background: linear-gradient(135deg, #f5f7fa 0%, #e8eef7 100%);
    }

    /* Main title */
    .main-title {
        font-size: 42px;
        font-weight: 800;
        text-align: center;
        margin-bottom: 5px;
        color: #1f2937;
    }

    .subtitle {
        text-align: center;
        font-size: 18px;
        color: #64748b;
        margin-bottom: 30px;
    }

    /* Section headings */
    .section-title {
        font-size: 24px;
        font-weight: 700;
        color: #1f2937;
        margin-top: 20px;
        margin-bottom: 15px;
    }

    /* Metric cards */
    .metric-card {
        background: white;
        padding: 18px;
        border-radius: 14px;
        text-align: center;
        box-shadow: 0 4px 15px rgba(0,0,0,0.08);
        border: 1px solid #e5e7eb;
    }

    .metric-value {
        font-size: 27px;
        font-weight: 800;
        color: #2563eb;
    }

    .metric-label {
        font-size: 14px;
        color: #64748b;
        margin-top: 5px;
    }

    /* Prediction result */
    .result-box {
        padding: 25px;
        border-radius: 16px;
        text-align: center;
        margin-top: 25px;
        background: white;
        box-shadow: 0 5px 20px rgba(0,0,0,0.10);
    }

    .result-title {
        font-size: 27px;
        font-weight: 800;
        margin-bottom: 8px;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #ffffff;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        border-radius: 10px;
        height: 50px;
        font-size: 18px;
        font-weight: 700;
    }

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------------
# SIDEBAR - MODEL INFORMATION
# ---------------------------------------------------------
with st.sidebar:

    st.header("📊 Model Information")

    st.write("### Machine Learning Model")

    st.write("**Algorithm:** Logistic Regression")
    st.write("**Task:** Customer Churn Prediction")

    st.divider()

    st.write("### 📈 Model Performance")

    st.metric("Accuracy", "80.06%")
    st.metric("Precision", "64.76%")
    st.metric("Recall", "54.55%")
    st.metric("F1 Score", "59.22%")

    st.divider()

    st.write("### 🔮 Prediction Classes")

    st.success("0 → Customer is not likely to churn")
    st.error("1 → Customer is likely to churn")

    st.divider()

    st.caption(
        "The model analyzes customer demographic, service, "
        "contract, and billing information to predict churn."
    )


# ---------------------------------------------------------
# MAIN HEADER
# ---------------------------------------------------------
st.markdown(
    '<div class="main-title">📊 Customer Churn Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Machine Learning powered customer retention analysis'
    '</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# MODEL PERFORMANCE CARDS
# ---------------------------------------------------------
st.markdown(
    '<div class="section-title">📈 Model Performance</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">80.06%</div>
        <div class="metric-label">Accuracy</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">64.76%</div>
        <div class="metric-label">Precision</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">54.55%</div>
        <div class="metric-label">Recall</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown("""
    <div class="metric-card">
        <div class="metric-value">59.22%</div>
        <div class="metric-label">F1 Score</div>
    </div>
    """, unsafe_allow_html=True)


# ---------------------------------------------------------
# CUSTOMER INFORMATION
# ---------------------------------------------------------
st.markdown(
    '<div class="section-title">👤 Customer Information</div>',
    unsafe_allow_html=True
)


# ---------------------------------------------------------
# NUMERICAL INPUTS
# ---------------------------------------------------------
st.subheader("💰 Customer & Billing Details")

col1, col2, col3 = st.columns(3)

with col1:
    tenure = st.number_input(
        "Tenure (Months)",
        min_value=0,
        max_value=100,
        value=12
    )

with col2:
    MonthlyCharges = st.number_input(
        "Monthly Charges",
        min_value=0.0,
        value=50.0
    )

with col3:
    TotalCharges = st.number_input(
        "Total Charges",
        min_value=0.0,
        value=500.0
    )


# ---------------------------------------------------------
# PERSONAL INFORMATION
# ---------------------------------------------------------
st.subheader("👤 Personal Information")

col1, col2, col3, col4 = st.columns(4)

with col1:
    gender = st.selectbox(
        "Gender",
        ["Female", "Male"]
    )

with col2:
    SeniorCitizen = st.selectbox(
        "Senior Citizen",
        [0, 1]
    )

with col3:
    Partner = st.selectbox(
        "Partner",
        ["No", "Yes"]
    )

with col4:
    Dependents = st.selectbox(
        "Dependents",
        ["No", "Yes"]
    )


# ---------------------------------------------------------
# PHONE & INTERNET SERVICES
# ---------------------------------------------------------
st.subheader("📱 Phone & Internet Services")

col1, col2, col3 = st.columns(3)

with col1:
    PhoneService = st.selectbox(
        "Phone Service",
        ["No", "Yes"]
    )

with col2:
    MultipleLines = st.selectbox(
        "Multiple Lines",
        ["No", "Yes"]
    )

with col3:
    InternetService = st.selectbox(
        "Internet Service",
        ["DSL", "Fiber optic", "No"]
    )


# ---------------------------------------------------------
# ONLINE SERVICES
# ---------------------------------------------------------
st.subheader("🔐 Online Services")

col1, col2, col3, col4 = st.columns(4)

with col1:
    OnlineSecurity = st.selectbox(
        "Online Security",
        ["No", "Yes", "No internet service"]
    )

with col2:
    OnlineBackup = st.selectbox(
        "Online Backup",
        ["No", "Yes", "No internet service"]
    )

with col3:
    DeviceProtection = st.selectbox(
        "Device Protection",
        ["No", "Yes", "No internet service"]
    )

with col4:
    TechSupport = st.selectbox(
        "Tech Support",
        ["No", "Yes", "No internet service"]
    )


# ---------------------------------------------------------
# STREAMING SERVICES
# ---------------------------------------------------------
st.subheader("📺 Streaming Services")

col1, col2 = st.columns(2)

with col1:
    StreamingTV = st.selectbox(
        "Streaming TV",
        ["No", "Yes", "No internet service"]
    )

with col2:
    StreamingMovies = st.selectbox(
        "Streaming Movies",
        ["No", "Yes", "No internet service"]
    )


# ---------------------------------------------------------
# CONTRACT & PAYMENT
# ---------------------------------------------------------
st.subheader("💳 Contract & Payment")

col1, col2 = st.columns(2)

with col1:
    Contract = st.selectbox(
        "Contract",
        ["Month-to-month", "One year", "Two year"]
    )

with col2:
    PaymentMethod = st.selectbox(
        "Payment Method",
        [
            "Electronic check",
            "Mailed check",
            "Bank transfer (automatic)",
            "Credit card (automatic)"
        ]
    )

PaperlessBilling = st.selectbox(
    "Paperless Billing",
    ["No", "Yes"]
)


# ---------------------------------------------------------
# PREDICTION BUTTON
# ---------------------------------------------------------
st.markdown("---")

predict_button = st.button(
    "🔮 Predict Customer Churn"
)


# ---------------------------------------------------------
# PREDICTION
# ---------------------------------------------------------
if predict_button:

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

    result, churn_probability = predict_churn(customer_data)

    st.markdown("---")
    st.subheader("🔮 Prediction Result")

    if "not likely" in result.lower():

        st.success("✅ Customer is not likely to churn.")

        st.info(
            "The model predicts that this customer is likely to remain with the company."
        )

    else:

        st.error("⚠️ Customer is likely to churn.")

        st.warning(
            "Recommendation: Consider discounts, loyalty plans, "
            "or personalized retention offers."
      )

    st.write(
        f"**Churn Probability: {churn_probability * 100:.2f}%**"
    )

    st.progress(churn_probability)
# ---------------------------------------------------------
# FOOTER
# ---------------------------------------------------------
st.markdown("---")

st.caption(
    "Customer Churn Prediction • Logistic Regression • "
    "Machine Learning Project"
)