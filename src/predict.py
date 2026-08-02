import pandas as pd

from src.model import model
from src.preprocess import preprocess_data
from src.utils import get_prediction_message

def predict_churn(input_data):
    """
    Predict whether a customer will churn.
    """

    input_df = pd.DataFrame([input_data])

    print(input_df.columns.tolist())

    processed_data = preprocess_data(input_df)

    prediction = model.predict(processed_data)

    return get_prediction_message(prediction[0])