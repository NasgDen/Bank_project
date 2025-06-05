import json
import logging
import os

PATH_TO_LOG_FILE = os.path.join(os.getcwd(), "logs", "utils.log")
utils_log = logging.getLogger(__name__)
utils_log.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_log.addHandler(file_handler)


def read_json(path_to_json: str) -> list[dict]:
    """
    Функция принимает на вход путь до JSON-файла и возвращает список словарей с данными о финансовых транзакциях
    :param path_to_json: путь до json файла
    :return transactions: список транзакций
    """
    utils_log.debug(f"Вызов функции {read_json.__name__}")
    try:
        with open(path_to_json, mode="r", encoding="utf-8") as file:
            transactions = json.load(file)
            utils_log.info(f"Файл {path_to_json} успешно прочитан, данные записаны в переменную transactions")
            return transactions
    except FileNotFoundError:
        utils_log.error(f"Файл {path_to_json} не найден")
        utils_log.debug("В переменную transactions записываем пустой список")
        transactions = []
        return transactions
    except json.JSONDecodeError:
        utils_log.error(f"Файл {path_to_json} имеет неверный формат")
        utils_log.debug("В переменную transactions записываем пустой список")
        transactions = []
        return transactions
