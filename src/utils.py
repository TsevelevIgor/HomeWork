import json


def get_transactions():
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        with open('operations.json') as operations:
            try:
                transactions_data = json.loads(operations)
                return transactions_data
            except json.JSONDecodeError:
                transactions_data = []
                return transactions_data
    except FileNotFoundError:
        transactions_data = []
        return transactions_data
