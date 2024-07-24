import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State
import plotly.graph_objs as go
import numpy as np
import datetime
import socket

from src.data_fetcher import DataFetcher
from src.volatility_calculator import VolatilityCalculator
from src.option_pricer import OptionPricer
from src.monte_carlo_simulator import MonteCarloSimulator
from src.risk_manager import RiskManager

class OptionsAnalysisApp:
    def __init__(self):
        self.app = dash.Dash(__name__)
        self.setup_layout()

    def setup_layout(self):
        self.app.layout = html.Div([
            html.H1("Advanced 0-DTE Options Analysis Dashboard"),
            dcc.Input(id="ticker-input", type="text", placeholder="Enter stock ticker", value="AAPL"),
            dcc.Dropdown(
                id="model-dropdown",
                options=[
                    {'label': 'Black-Scholes', 'value': 'black_scholes'},
                    {'label': 'Binomial Tree', 'value': 'binomial_tree'}
                ],
                value='black_scholes',
                style={'width': '200px'}
            ),
            dcc.Dropdown(
                id="timeframe-dropdown",
                options=[
                    {'label': '1 minutes', 'value': '1m'},
                    {'label': '5 minutes', 'value': '5m'},
                    {'label': '15 minutes', 'value': '15m'},
                    {'label': '30 minutes', 'value': '30m'},
                    {'label': '1 hour', 'value': '1h'}
                ],
                value='1m',
                style={'width': '200px'}
            ),
            html.Button('Analyze', id='analyze-button', n_clicks=0),
            dcc.Loading(
                id="loading",
                children=[html.Div(id="loading-output")],
                type="default",
            ),
            dcc.Graph(id="stock-price-chart"),
            dcc.Graph(id="option-price-chart"),
            dcc.Graph(id="monte-carlo-chart"),
            dcc.Graph(id="volatility-chart"),
            html.Div(id="greeks-output"),
            html.Div(id="risk-metrics-output")
        ])

        self.setup_callbacks()

    def setup_callbacks(self):
        @self.app.callback(
            [Output("stock-price-chart", "figure"),
             Output("option-price-chart", "figure"),
             Output("monte-carlo-chart", "figure"),
             Output("volatility-chart", "figure"),
             Output("greeks-output", "children"),
             Output("risk-metrics-output", "children"),
             Output("loading-output", "children")],
            [Input("analyze-button", "n_clicks")],
            [State("ticker-input", "value"),
             State("model-dropdown", "value"),
             State("timeframe-dropdown", "value")]
        )
        def update_charts(n_clicks, ticker, model, timeframe):
            if n_clicks == 0:
                return dash.no_update

            try:
                # Fetch and process data
                stock_data = DataFetcher.fetch_real_time_data(ticker, period="1d", interval=timeframe)
                returns = np.log(stock_data['Close'] / stock_data['Close'].shift(1)).dropna()
                
                simple_volatility = VolatilityCalculator.calculate_intraday_volatility(stock_data)
                garch_volatility = VolatilityCalculator.calculate_garch_volatility(returns)
                
                S = stock_data['Close'].iloc[-1]
                K = S  # At-the-money option
                T = (datetime.datetime.now().replace(hour=16, minute=0, second=0, microsecond=0) - datetime.datetime.now()).total_seconds() / (24 * 3600)  # Time to market close
                r = 0.01  # Assume 1% risk-free rate
                
                if model == 'black_scholes':
                    option_price = OptionPricer.black_scholes(S, K, T, r, garch_volatility)
                else:
                    option_price = OptionPricer.binomial_tree(S, K, T, r, garch_volatility, N=100)
                
                greeks = OptionPricer.calculate_greeks(S, K, T, r, garch_volatility)
                
                simulated_prices = MonteCarloSimulator.simulate_prices(S, T, r, garch_volatility)
                
                # Calculate risk metrics
                var = RiskManager.calculate_var(returns)
                cvar = RiskManager.calculate_cvar(returns)
                sharpe_ratio = RiskManager.calculate_sharpe_ratio(returns, r/252)
                
                # Create charts
                stock_chart = go.Figure(data=[go.Candlestick(x=stock_data.index,
                                                             open=stock_data['Open'],
                                                             high=stock_data['High'],
                                                             low=stock_data['Low'],
                                                             close=stock_data['Close'])])
                stock_chart.update_layout(title=f"{ticker} Stock Price ({timeframe} intervals)")
                
                option_chart = go.Figure(data=[go.Scatter(x=stock_data.index, y=stock_data['Close'].apply(lambda x: OptionPricer.black_scholes(x, K, T, r, garch_volatility)))])
                option_chart.update_layout(title="0-DTE Option Price")
                
                mc_chart = go.Figure(data=[go.Scatter(x=list(range(simulated_prices.shape[1])), y=path, mode='lines', opacity=0.1) for path in simulated_prices[:100]])
                mc_chart.add_trace(go.Scatter(x=list(range(simulated_prices.shape[1])), y=simulated_prices.mean(axis=0), mode='lines', name='Mean', line=dict(color='red', width=2)))
                mc_chart.update_layout(title="Monte Carlo Price Simulations (0-DTE)")
                
                volatility_chart = go.Figure(data=[
                    go.Scatter(x=stock_data.index, y=[simple_volatility]*len(stock_data), name='Simple Volatility'),
                    go.Scatter(x=stock_data.index, y=[garch_volatility]*len(stock_data), name='GARCH Volatility')
                ])
                volatility_chart.update_layout(title="Volatility Comparison")
                
                greeks_output = html.Div([
                    html.H3("0-DTE Option Greeks"),
                    html.P(f"Current Stock Price: ${S:.2f}"),
                    html.P(f"Option Price ({model.replace('_', ' ').title()}): ${option_price:.2f}"),
                    html.P(f"Time to Expiration: {T:.4f} days"),
                    html.P(f"Implied Volatility (GARCH): {garch_volatility:.2%}"),
                    html.P(f"Delta: {greeks['delta']:.4f}"),
                    html.P(f"Gamma: {greeks['gamma']:.4f}"),
                    html.P(f"Theta: {greeks['theta']:.4f}"),
                    html.P(f"Vega: {greeks['vega']:.4f}"),
                    html.P(f"Rho: {greeks['rho']:.4f}")
                ])
                
                risk_metrics_output = html.Div([
                    html.H3("Risk Metrics"),
                    html.P(f"Value at Risk (95% confidence): {var:.2%}"),
                    html.P(f"Conditional Value at Risk (95% confidence): {cvar:.2%}"),
                    html.P(f"Sharpe Ratio: {sharpe_ratio:.2f}")
                ])
                
                return stock_chart, option_chart, mc_chart, volatility_chart, greeks_output, risk_metrics_output, ""
            
            except Exception as e:
                return [dash.no_update] * 6 + [html.Div(f"Error: {str(e)}")]

    def find_free_port(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind(('', 0))
            s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            return s.getsockname()[1]

    def run(self, port=8050, debug=True, max_retries=5):
        for attempt in range(max_retries):
            try:
                self.app.run_server(port=port, debug=debug)
                break
            except OSError as e:
                if attempt < max_retries - 1:
                    print(f"Port {port} is in use. Trying a different port...")
                    port = self.find_free_port()
                else:
                    print(f"Failed to find an available port after {max_retries} attempts.")
                    print("Please close any applications using port 8050 or specify a different port.")
                    raise e

if __name__ == "__main__":
    app = OptionsAnalysisApp()
    app.run()
    