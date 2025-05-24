import pytest

from src.generator import card_number_generator, filter_by_currency, transaction_descriptions


# Тест test_filter_by_currency на корректные данные
def test_filter_by_currency(data, filter_by_currency_usd_1, filter_by_currency_usd_2, filter_by_currency_usd_3):
    iterator = filter_by_currency(data, "USD")
    assert next(iterator) == filter_by_currency_usd_1
    assert next(iterator) == filter_by_currency_usd_2
    assert next(iterator) == filter_by_currency_usd_3


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
def test_transaction_descriptions(data):
    trans_descrip = transaction_descriptions(data)
    assert next(trans_descrip) == "Перевод организации"
    assert next(trans_descrip) == "Перевод со счета на счет"
    assert next(trans_descrip) == "Перевод со счета на счет"
    assert next(trans_descrip) == "Перевод с карты на карту"


# Тест test_transaction_descriptions на пустой список
def test_transaction_descriptions_zero():
    with pytest.raises(StopIteration) as exc_info:
        trans_descrip = transaction_descriptions([])
        next(trans_descrip)
    assert "StopIteration" in str(exc_info)


# Тест test_card_number_generator на корректные данные
def test_card_number_generator():
    trans_descrip = card_number_generator(10, 15)
    assert next(trans_descrip) == "0000 0000 0000 0010"
    assert next(trans_descrip) == "0000 0000 0000 0011"
    assert next(trans_descrip) == "0000 0000 0000 0012"
    assert next(trans_descrip) == "0000 0000 0000 0013"
    assert next(trans_descrip) == "0000 0000 0000 0014"
    assert next(trans_descrip) == "0000 0000 0000 0015"


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
