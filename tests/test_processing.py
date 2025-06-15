from src.processing import filter_by_state, sort_by_date
from tests.conftest import list_of_dic_canceled, list_of_dic_executed, sort_by_date_ascending, sort_by_date_descending


# Тестирование функции filter_by_state с помощью Фикстур
def test_filter_by_state_executed(list_of_dic):
    assert filter_by_state(list_of_dic, "EXECUTED") == list_of_dic_executed()


def test_filter_by_state_canceled(list_of_dic):
    assert filter_by_state(list_of_dic, "CANCELED") == list_of_dic_canceled()


def test_filter_by_state_random(list_of_dic):
    assert filter_by_state(list_of_dic, "PROCESSED") == []


def test_filter_by_state_zero_dic():
    assert filter_by_state([], "CANCELED") == []


# Тестирование функции sort_by_date с помощью Фикстур
def test_sort_by_date_descending(list_of_dic):
    assert sort_by_date(list_of_dic, True) == sort_by_date_descending()


def test_sort_by_date_ascending(list_of_dic):
    assert sort_by_date(list_of_dic, False) == sort_by_date_ascending()


def test_sort_by_date_zero():
    assert sort_by_date([], False) == []


def test_sort_by_date_identical(sort_by_date_identical):
    assert sort_by_date(sort_by_date_identical) == sort_by_date_identical


