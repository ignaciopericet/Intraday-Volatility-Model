import pandas as pd
from src import (
    fetch_spx_data,
    calculate_intraday_volatility,
    monte_carlo_simulation,
    calculate_option_price,
    calculate_greeks,
    calculate_implied_volatility,
    plot_profit_loss_diagram,
    risk_management_report
)

def main():
    # Fetch SPX data for the last 20 years
    data = fetch_spx_data()
    
    # Ensure the 'date' column is in datetime format
    data['date'] = pd.to_datetime(data['date'])
    
    # Calculate intraday volatility
    volatility = calculate_intraday_volatility(data)
    
    # Perform Monte Carlo price simulations
    price_simulations = monte_carlo_simulation(data, volatility)
    
    # Calculate option price and greeks
    option_price = calculate_option_price(price_simulations)
    greeks = calculate_greeks(price_simulations)
    
    # Calculate implied volatility
    implied_volatility = calculate_implied_volatility(data)
    
    # Plot profit/loss diagram
    plot_profit_loss_diagram(option_price, greeks)
    
    # Generate risk management report
    risk_management_report(data, option_price, greeks)
    
    print("Intraday Volatility:", volatility)
    print("Option Price:", option_price)
    print("Greeks:", greeks)
    print("Implied Volatility:", implied_volatility)

if __name__ == "__main__":
    main()
