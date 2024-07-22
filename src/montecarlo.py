import numpy as np

def monte_carlo_simulation(data, volatility, num_simulations=1000, num_days=1):
    np.random.seed(42)
    daily_returns = np.random.normal(0, volatility/np.sqrt(252), (num_days, num_simulations))
    price_paths = np.exp(np.cumsum(daily_returns, axis=0))
    price_simulations = data['close'].iloc[-1] * price_paths
    return price_simulations
