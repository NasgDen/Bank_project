import pandas as pd


def read_cvs_file(path: str):
    """
    Функция принимает путь к файлу csv и считывает данные
    """
    result_csv = pd.read_csv(path)
    return result_csv


def read_excel_file(path: str):
    """
    Функция принимает путь к файлу excel и считывает данные
    """
    result_excel = pd.read_excel(path)
    return result_excel