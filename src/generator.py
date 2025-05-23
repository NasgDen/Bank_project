from typing import Generator, Iterator


def filter_by_currency(transaction: list[dict], code: str) -> Iterator[dict]:
    """
    Функция принимает на вход список словарей, представляющих транзакции.
    Возвращает итератор, который поочередно выдает транзакции, где валюта операции соответствует заданной.
    """
    filtered_currency = [trans for trans in transaction if trans["operationAmount"]["currency"].get("code") == code]
    return iter(filtered_currency)


def transaction_descriptions(transaction: list[dict]) -> Generator[None]:
    """
    Функция принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    """
    for trans in transaction:
        yield trans.get("description")


def card_number_generator(start: int, end: int) -> Generator[str, int, int | None]:
    """
    Генератор, который выдает номера банковских карт в формате XXXX XXXX XXXX XXXX, где X — цифра номера карты.
    Генератор может сгенерировать номера карт в заданном диапазоне от 0000 0000 0000 0001 до 9999 9999 9999 9999.
    Генератор должен принимать начальное и конечное значения для генерации диапазона номеров.
    """
    try:
        if start > 0 and end <= 9999999999999999:
            for index in range(start, end + 1):
                new_numb = str("0" * (16 - len(str(index)))) + str(index)
                yield " ".join([new_numb[i:i + 4] for i in range(0, len(new_numb), 4)])
        else:
            return 0
    except TypeError:
        return 0
