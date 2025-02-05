import pandas as pd

def handle_missing_values(data):
    """
    Handle missing values in the dataset by filling with the mean of each column.
    
    Parameters:
    - data (pd.DataFrame): The input DataFrame with missing values.

    Returns:
    - pd.DataFrame: The DataFrame with missing values handled.
    """
    # Fill missing values with the column mean
    data_filled = data.fillna(data.mean())
    return data_filled
