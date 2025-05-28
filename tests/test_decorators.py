from os import path, remove
from time import ctime

import pytest

from src.decorators import log


# Функция для теста декоратора log с выводом в консоль
@log()
def devide(a, b):
    return a / b


# Функция для теста декоратора log с выводом в файл
@log("log.txt")
def devide_file(a, b):
    return a / b


# Тест декоратора log с использованием capsys
def test_decorators_out(capsys):
    devide(10, 5)
    captured = capsys.readouterr()
    assert captured.out == f"""{ctime()}: Начало работы функции {devide.__name__}
{ctime()}: Функция {devide.__name__} успешно завершила работу
Передаваемые параметры ((10, 5), {{}})\n"""


# Тест декоратора log с использованием параметризации
@pytest.mark.parametrize("a, b, expected", [
    (10, 2, 5),
    ("A", "B", "TypeError"),
    (10, 0, "ZeroDivisionError")
])
def test_decorators(a, b, expected):
    assert devide(a, b) == expected


# Тест декоратора log с записью в файл
def test_decorators_file():
    start_time = ctime()
    devide_file(25, 5)
    end_time = ctime()
    assert path.exists("log.txt")
    with open("log.txt", mode="r", encoding="utf-8") as file:
        assert file.read() == f"""{start_time}: Начало работы функции {devide_file.__name__}
{end_time}: Функция {devide_file.__name__} успешно завершила работу
Передаваемые параметры ((25, 5), {{}})\n"""
    remove("log.txt")


# Тест декоратора log с записью в файл при возникновении ошибки
def test_decorators_file_error():
    start_time = ctime()
    devide_file(25, 0)
    assert path.exists("log.txt")
    with open("log.txt", mode="r", encoding="utf-8") as file:
        assert file.read() == f"""{start_time}: Ошибка в работе функции {devide_file.__name__}: ZeroDivisionError
Аргументы функции: ((25, 0), {{}})\n"""
    remove("log.txt")
