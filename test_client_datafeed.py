import unittest
from unittest.mock import patch
from client_datafeed import get_stock_price

class TestClientDatafeed(unittest.TestCase):
    @patch('requests.get')
    def test_get_stock_price_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {'price': 150.0}
        price = get_stock_price("AAPL")
        self.assertEqual(price, 150.0)

    @patch('requests.get')
    def test_get_stock_price_failure(self, mock_get):
        mock_get.return_value.status_code = 404
        with self.assertRaises(Exception) as context:
            get_stock_price("INVALID")
        self.assertTrue('Failed to fetch data' in str(context.exception))

if __name__ == "__main__":
    unittest.main()
