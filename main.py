import os

from src.external_api import get_convert_to_rub
from src.generator import card_number_generator, filter_by_currency, transaction_descriptions
from src.masks import get_mask_account, get_mask_card_number
from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations
from src.read_files import read_cvs_file, read_excel_file
from src.utils import read_json
from src.widget import get_date, mask_account_card

PATH_TO_JSON_FILE = os.path.join(os.getcwd(), "data", "operations.json")
PATH_TO_CSV_FILE = os.path.join(os.getcwd(), "data", "transactions.csv")
PATH_TO_EXCEL_FILE = os.path.join(os.getcwd(), "data", "transactions_excel.xlsx")

if __name__ == "__main__":
    # Список словарей для проверки функции filter_by_state
    list_of_dic = [
        {'id': 41428829, 'state': 'EXECUTED', 'date': '2019-07-03T18:35:29.512364'},
        {'id': 939719570, 'state': 'EXECUTED', 'date': '2018-06-30T02:08:58.425572'},
        {'id': 594226727, 'state': 'CANCELED', 'date': '2018-09-12T21:27:25.241689'},
        {'id': 615064591, 'state': 'CANCELED', 'date': '2018-10-14T08:21:33.419441'}
    ]
    transactions = (
        [
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {
                    "amount": "9824.07",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702"
            },
            {
                "id": 142264268,
                "state": "EXECUTED",
                "date": "2019-04-04T23:20:05.206878",
                "operationAmount": {
                    "amount": "79114.93",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 19708645243227258542",
                "to": "Счет 75651667383060284188"
            },
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {
                    "amount": "43318.34",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            },
            {
                "id": 895315941,
                "state": "EXECUTED",
                "date": "2018-08-19T04:27:37.904916",
                "operationAmount": {
                    "amount": "56883.54",
                    "currency": {
                        "name": "USD",
                        "code": "USD"
                    }
                },
                "description": "Перевод с карты на карту",
                "from": "Visa Classic 6831982476737658",
                "to": "Visa Platinum 8990922113665229"
            },
            {
                "id": 594226727,
                "state": "CANCELED",
                "date": "2018-09-12T21:27:25.241689",
                "operationAmount": {
                    "amount": "67314.70",
                    "currency": {
                        "name": "руб.",
                        "code": "RUB"
                    }
                },
                "description": "Перевод организации",
                "from": "Visa Platinum 1246377376343588",
                "to": "Счет 14211924144426031657"
            }
        ]
    )
    # Ввод данных о номере карты и счета
    card_number = input("Введите номер карты: ")
    account_number = input("Введите номер счета: ")
    user_card_or_account_number = input("Введите номер карты или счета: ")

    # Вывод работы функций
    print(f"Номер карты: {get_mask_card_number(card_number)}")
    print(f"Номер счета: {get_mask_account(account_number)}")
    print("Вывод работы функции mask_account_card:")
    print(mask_account_card(user_card_or_account_number))
    print("Вывод работы функции get_date:")
    print(get_date("2024-03-11T02:26:18.671407"))
    print("Вывод работы функции filter_by_state:")
    print(filter_by_state(list_of_dic, "EXECUTED"))
    print("Вывод работы функции sort_by_date:")
    print(sort_by_date(list_of_dic))

    print("Вывод работы функции filter_by_currency:")
    usd_transactions = filter_by_currency(transactions, "USD")
    try:
        for _ in range(5):
            print(next(usd_transactions))
    except StopIteration:
        print("Все итерации выполнены")

    print("Вывод работы функции transaction_descriptions:")
    descriptions = transaction_descriptions(transactions)
    try:
        for _ in range(5):
            print(next(descriptions))
    except StopIteration:
        print("Все итерации выполнены")

    print("Вывод работы функции card_number_generator:")
    for card_number in card_number_generator(10, 15):
        print(card_number)

    list_transactions = read_json(PATH_TO_JSON_FILE)
    if list_transactions:
        print(get_convert_to_rub(list_transactions[0]))

    read_cvs_file(PATH_TO_CSV_FILE)
    data = read_excel_file(PATH_TO_EXCEL_FILE)
    print(process_bank_search(data, "Вклад"))

    print(process_bank_operations(data, ['Перевод с карты на карту', 'Открытие вклада']))