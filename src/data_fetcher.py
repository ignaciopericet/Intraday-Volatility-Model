import yfinance as yf

class DataFetcher:
    @staticmethod
    def fetch_real_time_data(ticker, period="1d", interval="1m"):
        try:
            stock = yf.Ticker(ticker)
            data = stock.history(period=period, interval=interval)
            if data.empty:
                raise ValueError(f"No data available for ticker {ticker}")
            return data
        except Exception as e:
            raise ValueError(f"Error fetching data for {ticker}: {str(e)}")
