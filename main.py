import pandas as pd
from src.data_loader import load_data
from src.volatility import calculate_intraday_volatility
from src.monte_carlo import monte_carlo_simulation
from src.option_pricing import calculate_option_price
from src.greeks import calculate_greeks
from src.implied_volatility import calculate_implied_volatility
from src.profit_loss_diagram import plot_profit_loss_diagram
from src.risk_management import risk_management_report

def main():
    # Load data
    data = load_data('data/example_data.csv')

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
