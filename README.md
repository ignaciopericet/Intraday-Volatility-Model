# 0-DTE Options Analysis Dashboard

## Overview

The 0-DTE Options Analysis Dashboard is an advanced tool for analyzing zero days to expiration (0-DTE) options. It provides real-time data analysis, option pricing, risk metrics, and interactive visualizations to help traders make informed decisions in the fast-paced world of 0-DTE options trading.

![Dashboard Screenshot](assets/dashboard_screenshot.png)

## Features

- Real-time stock data fetching
- Intraday and GARCH volatility calculations
- Option pricing using Black-Scholes and Binomial Tree models
- Greeks calculations (Delta, Gamma, Theta, Vega, Rho)
- Monte Carlo price simulations
- Risk metrics including Value at Risk (VaR) and Conditional Value at Risk (CVaR)
- Interactive Dash web application with multiple charts and metrics displays

## Installation

1. Clone the repository:
   ```
   git clone git clone https://github.com/YOUR_USERNAME/intraday-volatility-model.git
   cd intraday-volatility-model
   ```

2. Create a virtual environment and activate it:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Run the main application:
   ```
   python main.py
   ```

2. Open a web browser and go to `http://localhost:8050` (or the URL displayed in the console).

3. Enter a stock ticker, select the pricing model and timeframe, then click "Analyze" to view the results.

For more detailed usage instructions, please refer to the [Usage Guide](docs/usage.md).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [yfinance] for providing stock data
- [Dash] for the interactive web application framework
- [ARCH] for GARCH volatility modeling
