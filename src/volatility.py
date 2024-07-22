import numpy as np
import pandas as pd

def calculate_intraday_volatility(data):
    returns = np.log(data['close'] / data['close'].shift(1)).dropna()
    intraday_volatility = np.std(returns) * np.sqrt(252)
    return intraday_volatility
