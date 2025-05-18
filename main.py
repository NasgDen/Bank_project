from src.masks import get_mask_account, get_mask_card_number
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    # Ввод данных о номере карты и счета
    card_number = int(input("Введите номер карты: "))
    account_number = int(input("Введите номер счета: "))
    user_card_or_account_number = input("Введите номер карты или счета: ")

    # Вывод работы функций
    print(f"Номер карты: {get_mask_card_number(card_number)}")
    print(f"Номер счета: {get_mask_account(account_number)}")
    print(mask_account_card(user_card_or_account_number))
    print(get_date("2024-03-11T02:26:18.671407"))
