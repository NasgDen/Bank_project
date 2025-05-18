def filter_by_state(list_of_dic: list, state="EXECUTED") -> list:
    """
    Функция принимает список словарей и опционально значение для ключа state (по умолчанию 'EXECUTED')
    Возвращает новый список словарей, содержащий только те словари,
    у которых ключ state соответствует указанному значению.
    """
    new_list_of_dic = []
    for dic in list_of_dic:
        if dic.get("state") == state:
            new_list_of_dic.append(dic)
    return new_list_of_dic


def sort_by_date(list_of_dic: list, descending=True) -> list:
    """
    Функция принимает список словарей и необязательный параметр, задающий порядок сортировки (по умолчанию — убывание)
    Функция возвращать новый список, отсортированный по дате.
    """
    return sorted(list_of_dic, key=lambda date: date.get("date"), reverse=descending)
