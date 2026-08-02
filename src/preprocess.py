import pandas as pd
from src.model import scaler, encoders

def preprocess_data(df):

    categorical_cols = [
        "gender",
        "Partner",
        "Dependents",
        "PhoneService",
        "MultipleLines",
        "InternetService",
        "OnlineSecurity",
        "OnlineBackup",
        "DeviceProtection",
        "TechSupport",
        "StreamingTV",
        "StreamingMovies",
        "Contract",
        "PaperlessBilling",
        "PaymentMethod"
    ]

    for col in categorical_cols:
        df[col] = encoders[col].transform(df[col])

    # Scale all features
    df = scaler.transform(df)

    return df