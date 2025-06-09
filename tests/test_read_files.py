from unittest.mock import patch

import pandas as pd

from src.read_files import read_cvs_file


# Тест функции read_cvs_file - отсутствие файла
@patch("pandas.read_csv", side_effect=FileNotFoundError)
def test_read_csv_file_not_found(mock_read_csv):
    assert read_cvs_file("test.csv") == []
    mock_read_csv.assert_called_once_with("test.csv", sep=";", header=0)


# Тест функции read_cvs_file - файл пустой
@patch("pandas.read_csv", side_effect=pd.errors.EmptyDataError)
def test_read_csv_file_EmptyDataError(mock_read_csv):
    assert read_cvs_file("test.csv") == []
    mock_read_csv.assert_called_once_with("test.csv", sep=";", header=0)


# Тест функции read_cvs_file - корректные данные
@patch("pandas.read_csv")
def test_read_csv_file(mock_read_csv):
    mock_read_csv.return_value = pd.DataFrame({'col1': [1, 2, 3], 'col2': [4, 5, 6]})
    assert read_cvs_file("test.csv") == [{'col1': 1, 'col2': 4}, {'col1': 2, 'col2': 5}, {'col1': 3, 'col2': 6}]
    mock_read_csv.assert_called_once_with("test.csv", sep=";", header=0)
