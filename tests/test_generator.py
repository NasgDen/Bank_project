import pytest
from src.generator import filter_by_currency, transaction_descriptions, card_number_generator


def test_filter_by_currency(data, filter_by_currency_usd_1, filter_by_currency_usd_2, filter_by_currency_usd_3):
    iterator = filter_by_currency(data, "USD")
    assert next(iterator) == filter_by_currency_usd_1
    assert next(iterator) == filter_by_currency_usd_2
    assert next(iterator) == filter_by_currency_usd_3

def test_filter_by_currency_no_code(data):
    with pytest.raises(StopIteration) as exc_info:
        iterator = filter_by_currency(data)
        next(iterator)
    assert str(exc_info) == "<ExceptionInfo StopIteration() tblen=1>"


def test_filter_by_currency_no_zero():
    with pytest.raises(StopIteration) as exc_info:
        iterator = filter_by_currency([])
        next(iterator)
    assert str(exc_info) == "<ExceptionInfo StopIteration() tblen=1>"


def test_transaction_descriptions(data):
    trans_descrip = transaction_descriptions(data)
    assert next(trans_descrip) == "Перевод организации"
    assert next(trans_descrip) == "Перевод со счета на счет"
    assert next(trans_descrip) == "Перевод со счета на счет"
    assert next(trans_descrip) == "Перевод с карты на карту"


def test_transaction_descriptions_zero():
    with pytest.raises(StopIteration) as exc_info:
        trans_descrip = transaction_descriptions([])
        next(trans_descrip)
    assert str(exc_info) == "<ExceptionInfo StopIteration() tblen=1>"


# @pytest.mark.parametrize("start, stop, expected", [
#     (10, 15, "0000 0000 0000 0010"),
#     (10, 15, "0000 0000 0000 0011"),
#     (10, 15, "0000 0000 0000 0012"),
#     (10, 15, "0000 0000 0000 0013"),
#     (10, 15, "0000 0000 0000 0014"),
#     (10, 15, "0000 0000 0000 0015"),
# ])
def test_card_number_generator():
    trans_descrip = card_number_generator(10, 15)
    assert next(trans_descrip) == "0000 0000 0000 0010"
    assert next(trans_descrip) == "0000 0000 0000 0011"
    assert next(trans_descrip) == "0000 0000 0000 0012"
    assert next(trans_descrip) == "0000 0000 0000 0013"

def test_card_number_generator_():
    with pytest.raises(StopIteration) as exc_info:
        card_num = card_number_generator("A", 10)
        next(card_num)
    assert str(exc_info) == "<ExceptionInfo StopIteration(0) tblen=1>"


def test_card_number_generator_big_number():
    with pytest.raises(StopIteration) as exc_info:
        card_num = card_number_generator(99999999999999999, 999999999999999999)
        next(card_num)
    assert str(exc_info) == "<ExceptionInfo StopIteration() tblen=1>"