import os
from dotenv import load_dotenv
import requests


load_dotenv('/.env')


def get_convert(transaction: dict) -> float:
    """Конвертирует 'USD' и 'EUR' в 'RUB' и выводит результат"""
    code = transaction["operationAmount"]["currency"]["code"]
    amount = transaction["operationAmount"]["amount"]
    if code == "RUB":
        return float(amount)
    elif code == "USD" or code == "EUR":
        url = f'https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={code}&amount={amount}'
        token_exchange = os.getenv('API_KEY')
        headers = {"apikey": token_exchange}
        response = requests.request("GET", url, headers=headers)
        result = response.json()
        return float(result['result'])
