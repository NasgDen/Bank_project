import pytest

from src.generator import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize("value, code, expected", [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
            "USD",
            {
                "id": 939719570,
                "state": "EXECUTED",
                "date": "2018-06-30T02:08:58.425572",
                "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                "description": "Перевод организации",
                "from": "Счет 75106830613657916952",
                "to": "Счет 11776614605963066702",
            }
        ),
        (
            [
                {
                    "id": 873106923,
                    "state": "EXECUTED",
                    "date": "2019-03-23T01:09:46.296404",
                    "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 44812258784861134719",
                    "to": "Счет 74489636417521191160"
                }
            ],
            "RUB",
            {
                "id": 873106923,
                "state": "EXECUTED",
                "date": "2019-03-23T01:09:46.296404",
                "operationAmount": {"amount": "43318.34", "currency": {"name": "руб.", "code": "RUB"}},
                "description": "Перевод со счета на счет",
                "from": "Счет 44812258784861134719",
                "to": "Счет 74489636417521191160"
            }
        )
    ]
)
# Тест test_filter_by_currency на корректные данные
def test_filter_by_currency(value, code, expected):
    assert next(filter_by_currency(value, code)) == expected


# Тест test_filter_by_currency на отсутствие ключа
def test_filter_by_currency_no_code(data):
    with pytest.raises(StopIteration) as exc_info:
        iterator = filter_by_currency(data)
        next(iterator)
    assert "StopIteration" in str(exc_info)


# Тест test_filter_by_currency на пустой список
def test_filter_by_currency_zero():
    with pytest.raises(StopIteration) as exc_info:
        iterator = filter_by_currency([])
        next(iterator)
    assert "StopIteration" in str(exc_info)


# Тест test_transaction_descriptions на корректные данные
@pytest.mark.parametrize(
    "value, expected",
    [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
            "Перевод организации",
        ),
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "operationAmount": {"amount": "9824.07", "currency": {"name": "USD", "code": "USD"}},
                    "description": "Перевод со счета на счет",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
            "Перевод со счета на счет",
        )
    ],
)
def test_transaction_descriptions(value, expected):
    trans_descrip = transaction_descriptions(value)
    assert next(trans_descrip) == expected


# Тест test_transaction_descriptions на пустой список
def test_transaction_descriptions_zero():
    with pytest.raises(StopIteration) as exc_info:
        trans_descrip = transaction_descriptions([])
        next(trans_descrip)
    assert "StopIteration" in str(exc_info)


# Тест test_card_number_generator на корректные данные
@pytest.mark.parametrize("start, stop, expected", [
    (10, 15, "0000 0000 0000 0010"),
    (99995555, 99995558, "0000 0000 9999 5555"),
    (1, 1, "0000 0000 0000 0001")
])
def test_card_number_generator(start, stop, expected):
    new_card = card_number_generator(start, stop)
    assert next(new_card) == expected


# Тест test_card_number_generator на некорректные данные
def test_card_number_generator_incorrect_data():
    with pytest.raises(StopIteration) as exc_info:
        card_num = card_number_generator("A", 10)
        next(card_num)
    assert "StopIteration" in str(exc_info)


# Тест test_card_number_generator на данные больше чем задано.
def test_card_number_generator_big_number():
    with pytest.raises(StopIteration) as exc_info:
        card_num = card_number_generator(99999999999999999, 999999999999999999)
        next(card_num)
    assert "StopIteration" in str(exc_info)
