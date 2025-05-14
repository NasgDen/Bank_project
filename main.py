from src.masks import get_mask_account, get_mask_card_number
from src.widget import mask_account_card

# Ввод данных о номере карты и счета
card_number = int(input("Введите номер карты: "))
account_number = int(input("Введите номер счета: "))
card_account_number = input("Введите номер счета или карты: ")

# Вывод работы функций
print(f"Номер карты: {get_mask_card_number(card_number)}")
print(f"Номер счета: {get_mask_account(account_number)}")
print(mask_account_card(card_account_number))
