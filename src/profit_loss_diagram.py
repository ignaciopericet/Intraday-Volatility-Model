import matplotlib.pyplot as plt
import numpy as np

def plot_profit_loss_diagram(option_price, greeks, strike_price=100):
    S = np.linspace(50, 150, 100)
    PnL = option_price + greeks['delta'] * (S - strike_price)

    plt.figure(figsize=(10, 5))
    plt.plot(S, PnL, label='Profit/Loss')
    plt.axhline(0, color='black', lw=2)
    plt.axvline(strike_price, color='red', linestyle='--', label='Strike Price')
    plt.xlabel('Underlying Price')
    plt.ylabel('Profit/Loss')
    plt.title('Profit/Loss Diagram')
    plt.legend()
    plt.show()
