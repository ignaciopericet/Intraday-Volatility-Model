import pandas as pd
import numpy as np
import yfinance as yf
import os

def fetch_spx_data(start_date='2003-07-15', end_date='2023-07-15', ticker='^GSPC'):
    """
    Fetch the historical data for the SPX (S&P 500) from Yahoo Finance.

    Parameters:
    start_date (str): The start date for fetching data in the format YYYY-MM-DD.
    end_date (str): The end date for fetching data in the format YYYY-MM-DD.
    ticker (str): The ticker symbol for the SPX (default is '^GSPC').

    Returns:
    pd.DataFrame: DataFrame containing the date, open, and close prices.
    """
    spx = yf.Ticker(ticker)
    hist = spx.history(start=start_date, end=end_date)
    
    # Select relevant columns and reset index to get 'date' as a column
    hist = hist[['Open', 'Close']].reset_index()
    
    # Rename columns
    hist.columns = ['date', 'open', 'close']
    
    # Ensure the data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Save to CSV
    try:
        hist.to_csv('data/example_data.csv', index=False)
        print("Data saved to 'data/example_data.csv'")
    except Exception as e:
        print(f"Failed to save data: {e}")
    
    return hist

def calculate_intraday_volatility(data, window=14):
    """
    Calculate the intraday volatility based on the last 14 days of price action.
    
    Parameters:
    data (pd.DataFrame): DataFrame with at least a 'date' and 'close' column.
    window (int): The window size for the rolling calculation (default is 14).
    
    Returns:
    pd.Series: Annualized intraday volatility.
    """
    # Ensure the data is sorted by date
    data = data.sort_values(by='date')
    
    # Calculate log returns
    data['log_return'] = np.log(data['close'] / data['close'].shift(1))
    
    # Calculate rolling volatility
    rolling_volatility = data['log_return'].rolling(window=window).std()
    
    # Annualize the volatility
    annualized_volatility = rolling_volatility * np.sqrt(252)
    
    # Drop NaN values
    annualized_volatility = annualized_volatility.dropna()
    
    return annualized_volatility

# Example usage
if __name__ == "__main__":
    # Fetch SPX data for the last 20 years
    data = fetch_spx_data()
    
    # Ensure the 'date' column is in datetime format
    data['date'] = pd.to_datetime(data['date'])
    
    # Calculate intraday volatility
    volatility = calculate_intraday_volatility(data)
    
    # Print or save the results
    print(volatility)
    
    # Ensure the data directory exists
    if not os.path.exists('data'):
        os.makedirs('data')
    
    # Save the results to a CSV file
    try:
        volatility.to_csv('data/annualized_volatility.csv', index=True)
        print("Volatility data saved to 'data/annualized_volatility.csv'")
    except Exception as e:
        print(f"Failed to save volatility data: {e}")


