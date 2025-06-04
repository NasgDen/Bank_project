import os

import requests
from dotenv import load_dotenv


def get_convert_to_rub(transactions):
    """
    Функция принимает на вход транзакцию и возвращает сумму транзакции в рублях, тип данных — float.
    Если транзакция была в USD или EUR, происходит обращение к внешнему API для получения текущего курса валют
    и конвертации суммы операции в рубли.
    """
    if ((transactions.get("operationAmount")).get("currency")).get("code") != "RUB":
        name = ((transactions.get("operationAmount")).get("currency")).get("code")
        amount = (transactions.get("operationAmount")).get("amount")
        path_env = os.path.join(os.getcwd(), ".env")
        load_dotenv(path_env)
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={name}&amount={amount}"
        payload = {}
        headers = {
          "apikey": f"{api_key}"
        }
        try:
            response = requests.get(url, headers=headers, data=payload)
        except requests.exceptions.ConnectionError:
            return "Ошибка подключения. Проверьте сетевое подключение."
        result = response.json()
        return round(result.get("result"), 2)
    else:
        return (transactions.get("operationAmount")).get("amount")
