import pytest

from src.widget import mask_account_card, get_date


@pytest.mark.parametrize('value, expected', [
    ('Visa Platinum 1234567890123456', 'Visa Platinum 1234 56 ** **** 3456'),
    ('Счет 12345678901234567890', 'Счет **7890'),
    ('Maestro 1111111111111111', 'Maestro 1111 11 ** **** 1111')
])
def test_mask_account_card(value, expected):
    assert mask_account_card(value) == expected

    with pytest.raises(ValueError):
        mask_account_card('VISA PLATINUM 1234567890123456')
        mask_account_card('1234567890123456')
        mask_account_card('Счет')
        mask_account_card('Visa 1234567890123456')
        mask_account_card('MasterCard 1')
        mask_account_card('MasterCard')
        mask_account_card('')


@pytest.mark.parametrize('value, expected', [
    ("2024-07-20T15:15:15.15151", '20.07.2024'),
    ('2023-01-31T23:59:59.15151', '31.01.2023'),
    ('2022-12-01T00:00:00.15151', '01.12.2022')
])
def test_get_date(value, expected):
    assert get_date(value) == expected
