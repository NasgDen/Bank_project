from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

# Ввод данных о номере карты и счета
card_number = int(input("Введите номер карты: "))
account_number = int(input("Введите номер счета: "))

# Вывод работы функций
print(f"Номер карты: {get_mask_card_number(card_number)}")
print(f"Номер счета: {get_mask_account(account_number)}")
print("Примеры входных данных для проверки функции mask_account_card")
print(mask_account_card("Maestro 1596837868705199"))
print(mask_account_card("Счет 64686473678894779589"))
print(mask_account_card("MasterCard 7158300734726758"))
print(mask_account_card("Счет 35383033474447895560"))
print(mask_account_card("Visa Classic 6831982476737658"))
print(mask_account_card("Visa Platinum 8990922113665229"))
print(mask_account_card("Visa Gold 5999414228426353"))
print(mask_account_card("Счет 73654108430135874305"))
print(get_date("2024-03-11T02:26:18.671407"))
