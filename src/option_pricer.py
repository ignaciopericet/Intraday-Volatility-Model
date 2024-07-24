import numpy as np
from scipy.stats import norm

class OptionPricer:
    @staticmethod
    def black_scholes(S, K, T, r, sigma, option_type="call"):
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        
        if option_type == "call":
            price = S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        else:
            price = K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        
        return price

    @staticmethod
    def binomial_tree(S, K, T, r, sigma, N, option_type="call"):
        dt = T / N
        u = np.exp(sigma * np.sqrt(dt))
        d = 1 / u
        p = (np.exp(r * dt) - d) / (u - d)
        
        ST = np.array([S * u**j * d**(N-j) for j in range(N+1)])
        
        if option_type == "call":
            C = np.maximum(ST - K, 0)
        else:
            C = np.maximum(K - ST, 0)
        
        for i in range(N-1, -1, -1):
            C = np.exp(-r * dt) * (p * C[1:] + (1-p) * C[:-1])
        
        return C[0]

    @staticmethod
    def calculate_greeks(S, K, T, r, sigma, option_type="call"):
        d1 = (np.log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        
        delta = norm.cdf(d1) if option_type == "call" else -norm.cdf(-d1)
        gamma = norm.pdf(d1) / (S * sigma * np.sqrt(T))
        theta = (-S * norm.pdf(d1) * sigma / (2 * np.sqrt(T)) 
                 - r * K * np.exp(-r * T) * norm.cdf(d2)) / 252
        vega = S * norm.pdf(d1) * np.sqrt(T) / 100
        rho = K * T * np.exp(-r * T) * norm.cdf(d2) / 100
        
        return {"delta": delta, "gamma": gamma, "theta": theta, "vega": vega, "rho": rho}