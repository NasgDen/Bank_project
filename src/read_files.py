import pandas as pd


def read_cvs_file(path: str) -> list[dict]:
    """
    Функция принимает путь к файлу csv, считывает данные и выводит список словарей.
    """
    try:
        result_csv = pd.read_csv(path, sep=";", header=0)
        return result_csv.to_dict("records")
    except (FileNotFoundError, pd.errors.EmptyDataError):
        return []


def read_excel_file(path: str) -> list[dict]:
    """
    Функция принимает путь к файлу excel, считывает данные и выводит список словарей.
    """
    try:
        result_excel = pd.read_excel(path)
        return result_excel.to_dict("records")
    except FileNotFoundError:
        return []
