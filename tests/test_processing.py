from src.processing import filter_by_state, sort_by_date, process_bank_search, process_bank_operations
from tests.conftest import list_of_dic_canceled, list_of_dic_executed, sort_by_date_ascending, sort_by_date_descending
import pytest


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


@pytest.mark.parametrize("value, string, expected", [
        (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "amount": "9824.07",
                    "currency_name": "USD",
                    "currency_code": "USD",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
              "Перевод",
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "amount": "9824.07",
                    "currency_name": "USD",
                    "currency_code": "USD",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                }
            ],
        )
    ]
)
def test_process_bank_search(value, string, expected):
    assert process_bank_search(value, string) == expected

def test_process_bank_search_zero_data():
    assert process_bank_search([], "Перевод") == []

def test_process_bank_search_zero_string():
    assert process_bank_search([{"id": 939719570, "description": "Перевод организации"}], "Открытие") == []


@pytest.mark.parametrize("value, words, expected", [
    (
            [
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "amount": "9824.07",
                    "currency_name": "USD",
                    "currency_code": "USD",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
                {
                    "id": 939719570,
                    "state": "EXECUTED",
                    "date": "2018-06-30T02:08:58.425572",
                    "amount": "9824.07",
                    "currency_name": "USD",
                    "currency_code": "USD",
                    "description": "Перевод организации",
                    "from": "Счет 75106830613657916952",
                    "to": "Счет 11776614605963066702",
                },
            ],
            ["Перевод организации"],
            {
                    "Перевод организации": 2
            }
    )
]
                         )
def test_process_bank_operations(value, words, expected):
    assert process_bank_operations(value, words) == expected



