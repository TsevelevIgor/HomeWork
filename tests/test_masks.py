import pytest


from src.masks import get_mask_card_number, get_mask_account


@pytest.mark.parametrize('value, expected', [
    (1000000000000000, '1000 00 ** **** 0000'),
    (1234567890123456, '1234 56 ** **** 3456'),
    (9999999999999999, '9999 99 ** **** 9999')
])
def test_get_mask_card_number(value, expected):
    assert get_mask_card_number(value) == expected

    with pytest.raises(ValueError):
        assert get_mask_card_number(111111111111111)
        assert get_mask_card_number(11111111111111111)
        assert get_mask_card_number()


@pytest.mark.parametrize('value, expected', [
    (10000000000000000000, '**0000'),
    (12345678901234567890, '**7890'),
    (99999999999999999999, '**9999')
])
def test_get_mask_account(value, expected):
    assert get_mask_account(value) == expected

    with pytest.raises(ValueError):
        assert get_mask_account(1234567890123456789)
        assert get_mask_account(123456789012345678901)
        assert get_mask_account()
