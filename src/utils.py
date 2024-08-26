import json
import logging


logger = logging.getLogger('utils')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/utils.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_transactions(file_path: str):
    """Принимает путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях"""
    try:
        logger.info('Обрабатываеться список словарей')
        with open(file_path, 'r', encoding='utf-8') as operations:
            try:
                logger.info('Выводиться список словарей')
                transactions_data = json.load(operations)
                return transactions_data
            except json.JSONDecodeError as ex:
                logger.error(f'Произошла ошибка: {ex}')
                transactions_data = []
                return transactions_data
    except FileNotFoundError as ex:
        logger.error(f'Произошла ошибка: {ex}')
        transactions_data = []
        return transactions_data
