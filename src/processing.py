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
