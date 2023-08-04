import unittest
from unittest.mock import patch
from flask_testing import TestCase
from forex_python.converter import RatesNotAvailableError

from app import app, get_rate

class FlaskAppTest(TestCase):
    def create_app(self):
        app.config['TESTING'] = True
        return app

    @patch('app.cr.get_rate')
    def test_get_rate_success(self, mock_get_rate):
        mock_get_rate.return_value = 1.2
        result = get_rate('CAD')
        self.assertTrue(result)

    @patch('app.cr.get_rate')
    def test_get_rate_fail(self, mock_get_rate):
        mock_get_rate.side_effect = RatesNotAvailableError
        result = get_rate('FAKE')
        self.assertFalse(result)

    @patch('app.cr.get_rates')
    def test_home_get(self, mock_get_rates):
        mock_get_rates.return_value = {'CAD': 1.0, 'EUR': 0.9}
        response = self.client.get('/')
        self.assert200(response)
        self.assertIn(b'CAD', response.data)
        self.assertIn(b'EUR', response.data)

    @patch('app.cr.convert')
    @patch('app.cr.get_rate')
    @patch('app.cc.get_symbol')
    @patch('app.flash') 
    def test_home_post(self, mock_flash, mock_get_symbol, mock_get_rate, mock_convert):
        mock_get_symbol.side_effect = ['$', '€']  # Returns '$' on first call and '€' on second call
        mock_get_rate.return_value = 1.2
        mock_convert.return_value = 120.0
        response = self.client.post('/', data={'from_currency': 'CAD', 'to_currency': 'EUR', 'amount': '100'})
        self.assert200(response)
        self.assert_template_used('home.html')
        # Check if the flash function was called with the expected message
        mock_flash.assert_called_once_with('$ 100.0 = € 120.00')


if __name__ == '__main__':
    unittest.main()



