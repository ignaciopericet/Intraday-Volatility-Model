import numpy as np

class MonteCarloSimulator:
    @staticmethod
    def simulate_prices(S, T, r, sigma, num_simulations=10000, num_steps=78):  # 78 5-minute intervals in a trading day
        dt = T / num_steps
        price_paths = np.zeros((num_simulations, num_steps + 1))
        price_paths[:, 0] = S
        
        for i in range(1, num_steps + 1):
            z = np.random.standard_normal(num_simulations)
            price_paths[:, i] = price_paths[:, i-1] * np.exp((r - 0.5 * sigma ** 2) * dt + sigma * np.sqrt(dt) * z)
        
        return price_paths