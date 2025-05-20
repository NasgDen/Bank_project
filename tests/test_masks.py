from src.masks import get_mask_account, get_mask_card_number
import pytest

@pytest.mark.parametrize("card_number, expected", [
    ("", "Неверный ввод номера карты"),
    ("1111222233334444", "1111 22** **** 4444"),
    ("5555999977771212", "5555 99** **** 1212"),
    ("22225555", "Неверный ввод номера карты"),
    ("AAABBBCCCDDD", "Неверный ввод номера карты")
])
def test_get_mask_card_number(card_number, expected):
    assert get_mask_card_number(card_number) == expected

def test_get_masks_card_number_fixture(card_number):
    assert get_mask_card_number(card_number) == "1236 56** **** 7231"
