from scipy.optimize import brentq

def black_scholes_call_price(S, K, T, r, sigma):
    from scipy.stats import norm
    from math import log, sqrt, exp

    d1 = (log(S / K) + (r + 0.5 * sigma ** 2) * T) / (sigma * sqrt(T))
    d2 = d1 - sigma * sqrt(T)
    return S * norm.cdf(d1) - K * exp(-r * T) * norm.cdf(d2)

def calculate_implied_volatility(market_price, S, K, T, r):
    objective_function = lambda sigma: market_price - black_scholes_call_price(S, K, T, r, sigma)
    implied_vol = brentq(objective_function, 0.001, 1.0)
    return implied_vol
