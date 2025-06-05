import logging
import os

PATH_TO_LOG_FILE = os.path.join(os.getcwd(), "logs", "masks.log")
masks_log = logging.getLogger(__name__)
masks_log.setLevel(logging.DEBUG)
file_handler = logging.FileHandler(PATH_TO_LOG_FILE, mode="w", encoding="utf-8")
file_formatter = logging.Formatter("%(asctime)s %(name)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
masks_log.addHandler(file_handler)


def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX.
    """
    masks_log.info(f"Вызов модуля {__name__}")
    if len(card_number) == 16 and card_number.isdigit():
        card_number_str = str(card_number)
        masks_log.debug(f"Номер введенной карты: {card_number_str}")
        return card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
    else:
        masks_log.warning("Введен не верный номер карты")
        return "Неверный ввод номера карты"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX
    """
    if len(account_number) == 20 and account_number.isdigit():
        account_number_str = str(account_number)
        masks_log.debug(f"Номер введенного счета: {account_number_str}")
        return "**" + account_number_str[-4:]
    else:
        masks_log.warning("Введен не верный номер счета")
        return "Неверный ввод номера счета"
