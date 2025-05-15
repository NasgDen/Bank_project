from .masks import get_mask_account, get_mask_card_number


def mask_account_card(card_account_number: str) -> str:
    """
    Функция принимает строку, содержащую тип и номер карты или счета.
    Возвращать строку с замаскированным номером.
    """
    index_digit = card_account_number.rfind(" ")
    if "Счет" in card_account_number[:index_digit]:
        mask_account = get_mask_account(int(card_account_number[index_digit + 1:]))
        return card_account_number[:index_digit + 1] + mask_account
    else:
        mask_card_number = get_mask_card_number(int(card_account_number[index_digit + 1:]))
        return card_account_number[:index_digit + 1] + mask_card_number


def get_date(date_time: str) -> str:
    """
    Функция принимает на вход строку с датой в формате "2024-03-11T02:26:18.671407"
    и возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    date = date_time[:date_time.find("T")].split(("-"))
    day = date[2]
    month = date[1]
    year = date[0]
    return day + "." + month + "." + year
