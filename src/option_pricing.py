import numpy as np
from scipy.stats import norm

def calculate_option_price(price_simulations, strike_price=100, option_type='call'):
    if option_type == 'call':
        payoff = np.maximum(0, price_simulations - strike_price)
    else:
        payoff = np.maximum(0, strike_price - price_simulations)
    
    option_price = np.mean(payoff) * np.exp(-0.05 * 1/252)
    return option_price
