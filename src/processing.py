import re
from collections import Counter

from src.decorators import log


@log()
def filter_by_state(list_of_dic: list, state="EXECUTED") -> list:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED')
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    return list(filter(lambda operation: operation.get("state") == state, list_of_dic))


def sort_by_date(list_of_dic: list, descending=True) -> list:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    Функция возвращать новый список, отсортированный по дате.
    """
    return sorted(list_of_dic, key=lambda date: date.get("date"), reverse=descending)


def process_bank_search(data: list[dict], search: str) -> list[dict]:
    """
    Функцию принимать список словарей с данными о банковских операциях и строку поиска.
    Возвращает список словарей, у которых в описании есть данная строка.
    """
    data_find = []
    for data_search in data:
        match = re.search(search, str(data_search["description"]), re.IGNORECASE)
        if match:
            data_find.append(data_search)
    return data_find


def process_bank_operations(data:list[dict], categories:list) -> dict:
    """
    Функцию принимать список словарей с данными о банковских операциях и список категорий операций.
    Возвращает словарь, в котором ключи — это названия категорий, а значения — это количество операций в каждой категории.
    """
    data_categories = {}
    categories_to_count = [item["description"] for item in data]
    categories_to_count = dict(Counter(categories_to_count))
    for category in categories:
        if category in categories_to_count:
            data_categories[category] = categories_to_count[category]
    return data_categories



