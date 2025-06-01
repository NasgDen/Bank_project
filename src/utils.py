import json


def read_json(path_to_json: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path_to_json: путь до json файла
    :return transactions: список транзакций
    """
    try:
        with open(path_to_json, mode="r", encoding="utf-8") as file:
            transactions = json.load(file)
            return transactions
    except (FileNotFoundError, json.JSONDecodeError):
        transactions = []
        return transactions
