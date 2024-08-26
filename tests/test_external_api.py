from unittest.mock import patch
from src.external_api import get_convert
import os


@patch("requests.get")
def test_external_api(mock_get):
    token_exchange = os.getenv('API_KEY')
    mock_get.return_value.json.return_value = {
        'success': True,
        'query':
            {'from': 'USD', 'to': 'RUB', 'amount': 30234.99},
        'info': {'timestamp': 1723453696, 'rate': 90.348788},
        'date': '2024-08-12',
        'result': 2731694.701692
    }
    assert get_convert({
        "id": 41428829,
        "state": "EXECUTED",
        "date": "2019-07-03T18:35:29.512364",
        "operationAmount": {
            "amount": "8221.37",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
            },
        "description": "Перевод организации",
        "from": "MasterCard 7158300734726758",
        "to": "Счет 35383033474447895560"
        })
    mock_get.assert_called_once_with(
            "GET",
            'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=8221.37',
            headers={"apikey": token_exchange})
