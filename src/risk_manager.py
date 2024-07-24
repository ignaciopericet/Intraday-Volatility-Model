import numpy as np

class RiskManager:
    @staticmethod
    def calculate_var(returns, confidence_level=0.95):
        return np.percentile(returns, (1 - confidence_level) * 100)

    @staticmethod
    def calculate_cvar(returns, confidence_level=0.95):
        var = RiskManager.calculate_var(returns, confidence_level)
        return returns[returns <= var].mean()

    @staticmethod
    def calculate_sharpe_ratio(returns, risk_free_rate):
        excess_returns = returns - risk_free_rate
        return np.sqrt(252) * excess_returns.mean() / excess_returns.std()