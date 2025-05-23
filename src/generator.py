from typing import Generator


def filter_by_currency(transaction: list[dict], code: str) -> Generator[dict]:
    for trans in transaction:
        if trans["operationAmount"]["currency"].get("code") == code:
            yield trans
