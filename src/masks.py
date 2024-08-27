import logging


logger = logging.getLogger('masks')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler('../logs/masks.log', encoding='utf-8')
file_formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s -%(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)


def get_mask_card_number(card_number: int) -> str:
    """ Функция принимает на вход номер карты и возвращает ее маску"""
    num = str(card_number)
    if len(num) != 16:
        logger.error('Неверное количество символов')
        raise ValueError("Неверное количество символов")
    logger.info('Маскируем номер карты')
    return f'{num[:4]} {num[4:6]} {"*" * 2} {"*" * 4} {num[12:]}'


def get_mask_account(account_number: int) -> str:
    """ Функция принимает на вход номер счета и возвращает его маску"""
    num = str(account_number)
    if len(num) != 20:
        logger.error('Неверное количество символов')
        raise ValueError("Неверное количество символов")
    logger.info('Маскируем номер счета')
    return "*" * 2 + num[- 4:]
