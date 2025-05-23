from typing import Generator, Any


def filter_by_currency(transaction: list[dict], code: str) -> Generator[dict]:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
    """
    for trans in transaction:
        if trans["operationAmount"]["currency"].get("code") == code:
            yield trans


def transaction_descriptions(transaction: list[dict]) -> Generator[None]:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for trans in transaction:
        yield trans.get("description")
