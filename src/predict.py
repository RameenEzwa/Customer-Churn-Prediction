import pandas as pd

from src.model import model
from src.preprocess import preprocess_data
from src.utils import get_prediction_message


def predict_churn(input_data):
    """
    Predict whether a customer will churn and return
    the prediction message and churn probability.
    """

    input_df = pd.DataFrame([input_data])

    processed_data = preprocess_data(input_df)

    prediction = model.predict(processed_data)

    probability = model.predict_proba(processed_data)[0][1]

    message = get_prediction_message(prediction[0])

    return message, probability