from src.masks import get_mask_account, get_mask_card_number

# Ввод данных о номере карты и счета
card_number = int(input("Введите номер карты: "))
account_number = int(input("Введите номер счета: "))

# Вывод работы функций
print(f"Номер карты: {get_mask_card_number(card_number)}")
print(f"Номер счета: {get_mask_account(account_number)}")
