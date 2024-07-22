import unittest
from src.volatility import calculate_intraday_volatility
import pandas as pd

class TestVolatility(unittest.TestCase):
    def test_calculate_intraday_volatility(self):
        data = pd.DataFrame({'close': [100, 101, 102, 101, 99, 100]})
        result = calculate_intraday_volatility(data)
        self.assertAlmostEqual(result, 0.064, places=3)

if __name__ == '__main__':
    unittest.main()
