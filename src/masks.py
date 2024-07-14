def get_mask_card_number(card_number: int) -> str:
    """ Функция принимает на вход номер карты и возвращает ее маску"""
    if len(str(card_number)) == 16:
        raise ValueError
    return f'{card_number[:4]} {card_number[4:6]} {"*" * 2} {"*" * 4} {card_number[12:]}'


def get_mask_account(account_number: int) -> str:
    """ Функция принимает на вход номер счета и возвращает его маску"""
    if len(str(account_number)) == 20:
        raise ValueError
    return f'{"*" * 2} {account_number[- 4::]}'


print(get_mask_card_number(1111111111111111))
print(get_mask_account(11111111111111111111))
