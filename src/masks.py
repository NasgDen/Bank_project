# from src.decorators import log
#
# @log()
def get_mask_card_number(card_number: str) -> str:
    """
    Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX.
    """
    if len(card_number) == 16 and card_number.isdigit():
        card_number_str = str(card_number)
        return card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]
    else:
        return "Неверный ввод номера карты"


def get_mask_account(account_number: str) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX
    """
    if len(account_number) == 20 and account_number.isdigit():
        account_number_str = str(account_number)
        return "**" + account_number_str[-4:]
    else:
        return "Неверный ввод номера счета"
