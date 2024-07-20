from src.masks import get_mask_account, get_mask_card_number
from datetime import datetime


def mask_account_card(account_card: str) -> str:
    """Функция принимает счёт или номер карты и возвращает маску"""
    card_name = ['MasterCard', 'Maestro', 'Visa Classic', 'Visa Platinum', 'Visa Gold']
    split_name = account_card.split()
    attached_name = ' '.join(split_name[0:2])
    if attached_name or split_name[-2] in card_name:
        if len(split_name[-1]) == 16:
            num = get_mask_card_number(int(account_card.split()[-1]))
            return f'{account_card[:-16]}{num}'
        elif len(split_name[-1]) == 20 and split_name[-2] == 'Счет':
            num = get_mask_account(int(split_name[-1]))
            return f'{account_card[:-20]}{num}'
        else:
            raise ValueError("Неверное количество символов")
    else:
        raise ValueError("Неверное количество символов")


def get_date(old_date: str) -> str:
    """Функция принимает строку с датой и выводит в формате ДД.ММ.ГГГГ"""
    new_date = datetime.strptime(old_date, "%Y-%m-%dT%H:%M:%S.%f")
    return new_date.strftime("%d.%m.%Y")
