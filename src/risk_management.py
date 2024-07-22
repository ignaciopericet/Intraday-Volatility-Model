def risk_management_report(data, option_price, greeks):
    # Simplified risk management report
    print("Risk Management Report")
    print("======================")
    print(f"Initial Option Price: {option_price}")
    print(f"Delta: {greeks['delta']}")
    print(f"Gamma: {greeks['gamma']}")
    print(f"Vega: {greeks['vega']}")
    print(f"Theta: {greeks['theta']}")
    print(f"Rho: {greeks['rho']}")
    print(f"Current Price: {data['close'].iloc[-1]}")
    print("======================")
