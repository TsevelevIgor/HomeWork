def get_mask_card_number(card_number: int) -> str:
    """ Функция принимает на вход номер карты и возвращает ее маску"""
    num = str(card_number)
    if len(num) != 16:
        raise ValueError("Неверное количество символов")
    return f'{num[:4]} {num[4:6]} {"*" * 2} {"*" * 4} {num[12:]}'


def get_mask_account(account_number: int) -> str:
    """ Функция принимает на вход номер счета и возвращает его маску"""
    num = str(account_number)
    if len(num) != 20:
        raise ValueError("Неверное количество символов")
    return "*" * 2 + num[- 4:]
