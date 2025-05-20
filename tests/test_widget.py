import pytest
from src.widget import mask_account_card, get_date


@pytest.mark.parametrize("card_account_card, expected", [
    ("", "Неверный ввод номера карты"),
    ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
    ("Счет 64686473678894779589", "Счет **9589"),
    ("MasterCard 7158300734726758", "MasterCard 7158 30** **** 6758"),
    ("Visa Classic 6831982476737658", "Visa Classic 6831 98** **** 7658"),
    ("Счет64686473678894779589", "Неверный ввод номера счета"),
    ("Счет 64686473a788947b9589", "Неверный ввод номера счета"),
    ("Visa Gold 22225555", "Неверный ввод номера карты"),
    ("Visa Platinum8990922113665229", "Неверный ввод номера карты"),
    ("AAABBBCCCDDD", "Неверный ввод номера карты")
])
def test_mask_account_card(card_account_card, expected):
    assert mask_account_card(card_account_card) == expected

@pytest.mark.parametrize("date_time, expected", [
    ("2024-03-11T02:26:18.671407", "11.03.2024"),
    ("2024 03 11 02:26:18.671407", "Неправильный формат даты"),
    ("2024 03 11T02:26:18.671407", "Неправильный формат даты"),
    ("2024-03-11 02:26:18.671407", "Неправильный формат даты"),
    ("2022-01-13T02:26:18.671407", "13.01.2022")
])
def test_get_date(date_time, expected):
    assert get_date(date_time) == expected