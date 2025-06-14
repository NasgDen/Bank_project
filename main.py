import os

from src.generator import filter_by_currency
from src.processing import filter_by_state, process_bank_search, sort_by_date
from src.read_files import read_cvs_file, read_excel_file
from src.utils import read_json
from src.widget import get_date, mask_account_card

PATH_TO_JSON_FILE = os.path.join(os.getcwd(), "data", "operations.json")
PATH_TO_CSV_FILE = os.path.join(os.getcwd(), "data", "transactions.csv")
PATH_TO_EXCEL_FILE = os.path.join(os.getcwd(), "data", "transactions_excel.xlsx")


def main():
    while True:
        print("""
Привет! Добро пожаловать в программу работы с банковскими транзакциями.
Выберите необходимый пункт меню:
1. Получить информацию о транзакциях из JSON-файла
2. Получить информацию о транзакциях из CSV-файла
3. Получить информацию о транзакциях из XLSX-файла
    """)
        select = input("> ")
        if select == "1":
            print("Для обработки выбран JSON-файл.")
            data = read_json(PATH_TO_JSON_FILE)
            break
        elif select == "2":
            print("Для обработки выбран CSV-файл.")
            data = read_cvs_file(PATH_TO_CSV_FILE)
            break
        elif select == "3":
            print("Для обработки выбран XLSX-файл.")
            data = read_excel_file(PATH_TO_EXCEL_FILE)
            break
        else:
            print("Неверный ввод данных")

    while True:
        print("Введите статус, по которому необходимо выполнить фильтрацию.")
        print("Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING")
        select_state = input("> ").upper()
        if select_state in ["EXECUTED", "CANCELED", "PENDING"]:
            print(f"Операции отфильтрованы по статусу {select_state}")
            filter_data = filter_by_state(data, select_state)
            break
        else:
            print(f"Статус операции '{select_state}' недоступен.")

    while True:
        print("Отсортировать операции по дате? Да/Нет")
        select = input("> ").lower()
        if select == "да":
            print("Отсортировать по возрастанию или по убыванию?")
            select = input("> ").lower()
            if select == "по возрастанию":
                sorted_data = sort_by_date(filter_data, False)
                print(sorted_data)
                break
            elif select == "по убыванию":
                sorted_data = sort_by_date(filter_data, True)
                break
            else:
                print("Введены неверные данные")
        elif select == "нет":
            sorted_data = filter_data
            break
        else:
            print("Введены неверные данные")

    while True:
        print("Выводить только рублевые транзакции? Да/Нет")
        select = input("> ").lower()
        if select == "да":
            filter_data_by_rub = filter_by_currency(sorted_data, "RUB")
            break
        if select == "нет":
            filter_data_by_rub = sorted_data
            break
        else:
            print("Введены неверные данные")

    while True:
        print("Отфильтровать список транзакций по определенному слову в описании? Да/Нет")
        select = input("> ")
        if select == "да":
            word_description = input("Введите слово для фильтрации транзакций: ")
            result_data = process_bank_search(filter_data_by_rub, word_description)
            break
        elif select == "нет":
            result_data = filter_data_by_rub
            break
        else:
            print("Введены неверные данные")

    print("Распечатываю итоговый список транзакций...")

    if len(list(result_data)) > 0:
        print(f"Всего банковских операций в выборке: {len(list(result_data))}")
        for data in result_data:
            print(f"{get_date(data["date"])} {data["description"]}")
            if str(data["description"]) == "Открытие вклада":
                print(mask_account_card(str(data["to"])))
            else:
                print(f"{mask_account_card(str(data["from"]))} -> {mask_account_card(str(data["to"]))}")
            print(f"Сумма: {(data["amount"])} {(data["currency_code"])}\n")
    else:
        print("Не найдено ни одной транзакции, подходящей под ваши условия фильтрации")


if __name__ == "__main__":
    main()
