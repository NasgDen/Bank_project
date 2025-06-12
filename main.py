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
                print(sorted_data)
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



if __name__ == "__main__":
    main()
