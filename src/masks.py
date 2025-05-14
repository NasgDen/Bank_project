def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает на вход номер карты в виде числа и возвращает маску номера по правилу XXXX XX** **** XXXX.
    """
    card_number_str = str(card_number)
    return card_number_str[:4] + " " + card_number_str[4:6] + "** **** " + card_number_str[-4:]


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает на вход номер счета в виде числа и возвращает маску номера по правилу **XXXX
    """
    account_number_str = str(account_number)
    return "**" + account_number_str[-4:]
