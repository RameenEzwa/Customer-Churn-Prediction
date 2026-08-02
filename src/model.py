import joblib

model = joblib.load("models/churn_model.joblib")

scaler = joblib.load("models/scaler.joblib")

encoders = joblib.load("models/label_encoders.joblib")