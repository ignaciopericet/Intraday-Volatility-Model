# 0-DTE Options Analysis Dashboard - Usage Guide

This guide will help you use the 0-DTE Options Analysis Dashboard effectively.

## Starting the Application

1. Ensure you have installed all required dependencies by running:
   ```
   pip install -r requirements.txt
   ```

2. From the root directory of the project, run:
   ```
   python main.py
   ```

3. Open a web browser and navigate to `http://localhost:8050` (or the URL displayed in the console).

## Using the Dashboard

1. Enter a stock ticker symbol (e.g., AAPL, GOOGL) in the input field.

2. Select the desired option pricing model:
   - Black-Scholes
   - Binomial Tree

3. Choose the timeframe for the analysis:
   - 1 minute
   - 5 minutes
   - 15 minutes
   - 30 minutes
   - 1 hour

4. Click the "Analyze" button to generate the analysis.

5. The dashboard will display:
   - Stock price chart
   - Option price chart
   - Monte Carlo price simulations
   - Volatility comparison
   - Option Greeks
   - Risk metrics

## Interpreting the Results

- The stock price chart shows the recent price movement of the selected stock.
- The option price chart displays the theoretical price of a 0-DTE at-the-money option.
- The Monte Carlo simulation shows potential price paths and their average.
- The volatility comparison chart shows simple historical volatility vs GARCH volatility.
- The Option Greeks provide sensitivity measures for the option.
- Risk metrics include Value at Risk (VaR), Conditional VaR, and Sharpe Ratio.

Remember that this tool is for educational and informational purposes only. Always consult with a financial advisor before making investment decisions.