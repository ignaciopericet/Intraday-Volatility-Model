def calculate_greeks(price_simulations, strike_price=100, option_type='call'):
    # Assuming simple estimations for demonstration
    delta = (price_simulations > strike_price).mean() if option_type == 'call' else (price_simulations < strike_price).mean()
    gamma = (price_simulations > strike_price).std() if option_type == 'call' else (price_simulations < strike_price).std()
    vega = delta * 0.01  # Simplified calculation
    theta = delta / 252  # Simplified calculation
    rho = delta * 0.01  # Simplified calculation
    return {"delta": delta, "gamma": gamma, "vega": vega, "theta": theta, "rho": rho}
