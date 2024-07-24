import numpy as np
from arch import arch_model

class VolatilityCalculator:
    @staticmethod
    def calculate_intraday_volatility(stock_data):
        returns = np.log(stock_data['Close'] / stock_data['Close'].shift(1))
        return returns.std() * np.sqrt(252 * 78)  # Assuming 78 5-minute intervals in a trading day

    @staticmethod
    def calculate_garch_volatility(returns, p=1, q=1):
        model = arch_model(returns, vol='Garch', p=p, q=q)
        results = model.fit(disp='off')
        forecast = results.forecast(horizon=1)
        return np.sqrt(forecast.variance.values[-1][0])