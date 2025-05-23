import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("card_number, expected", [
    ("", "Неверный ввод номера карты"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("5555999977771212", "5555 99** **** 1212"),
    ("22225555", "Неверный ввод номера карты"),
    ("AAABBBCCCDDD", "Неверный ввод номера карты")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected


@pytest.mark.parametrize("account, expected", [
    ("", "Неверный ввод номера счета"),
    ("11254854965321659523", "**9523"),
    ("36951475369852147856", "**7856"),
    ("22225555", "Неверный ввод номера счета"),
    ("12645FCDV453gFV34h4F", "Неверный ввод номера счета")
])
def test_get_mask_account(account, expected):
    assert get_mask_account(account) == expected
