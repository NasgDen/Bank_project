import os
from unittest.mock import patch

import requests
from dotenv import load_dotenv

from src.external_api import get_convert_to_rub

path_env = os.path.join(os.getcwd(), ".env")
load_dotenv(path_env)
api_key = os.getenv("API_KEY")
payload: dict = {}
headers = {
    "apikey": f"{api_key}"
}
url = "https://api.apilayer.com/exchangerates_data/convert?to=RUB&from=USD&amount=1"


@patch("requests.get")
def test_get_convert_to_rub(mock_get, test_dict_usd):
    mock_get.return_value.json.return_value = {"result": 1}
    assert get_convert_to_rub(test_dict_usd) == 1
    mock_get.assert_called_once_with(url, headers=headers, data=payload)


def test_get_convert_to_rub_rub(test_dict_rub):
    assert get_convert_to_rub(test_dict_rub) == 1


@patch("requests.get", side_effect=requests.ConnectionError)
def test_get_convert_to_rub_connect_error(mock_get, test_dict_usd):
    assert get_convert_to_rub(test_dict_usd) == 'Ошибка подключения. Проверьте сетевое подключение.'
    mock_get.assert_called_once_with(url, headers=headers, data=payload)
