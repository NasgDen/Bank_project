from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date
from src.widget import get_date, mask_account_card

if __name__ == "__main__":
    # Список словарей для проверки функции filter_by_state
    list_of_dic = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    # Ввод данных о номере карты и счета
    card_number = input("Введите номер карты: ")
    account_number = input("Введите номер счета: ")
    user_card_or_account_number = input("Введите номер карты или счета: ")

    # Вывод работы функций
    print(f"Номер карты: {get_mask_card_number(card_number)}")
    print(f"Номер счета: {get_mask_account(account_number)}")
    print(mask_account_card(user_card_or_account_number))
    print(get_date("2024 03 11T02:26:18.671407"))
    print(filter_by_state(list_of_dic, "EXECUTED"))
    print(sort_by_date(list_of_dic))
