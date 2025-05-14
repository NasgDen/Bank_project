from .masks import get_mask_card_number, get_mask_account

def mask_account_card(card_account_number:str) ->str:
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
