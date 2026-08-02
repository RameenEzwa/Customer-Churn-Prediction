"""
Utility functions for the Customer Churn Prediction project.
"""

def get_prediction_message(prediction):
    """
    Convert model prediction into a readable message.
    """
    if prediction == 1:
        return "Customer is likely to Churn."
    else:
        return "Customer is Not likely to Churn."