import pandas as pd
import numpy as np

def detect_outliers(data, column_name):
    """Detect outliers using Z-scores."""
    try:
        data['z_scores'] = np.abs((data[column_name] - data[column_name].mean()) / data[column_name].std())
        return data[data['z_scores'] > 3]  # Threshold Z-score to identify outliers
    except Exception as e:
        print(f"Error detecting outliers: {e}")
        return pd.DataFrame()

def filter_by_liquidity(data, column_name, threshold):
    """Filter markets by liquidity threshold."""
    try:
        return data[data[column_name] >= threshold]
    except Exception as e:
        print(f"Error filtering by liquidity: {e}")
        return pd.DataFrame()
