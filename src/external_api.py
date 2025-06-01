import os
from dotenv import load_dotenv, find_dotenv
import requests


def get_convert_to_rus(transactions:dict):

    path_env = os.path.join(os.getcwd(), ".env")
    load_dotenv(path_env)
    api_key = os.getenv("API_KEY")
    # print(api_key)

    if ((transactions.get("operationAmount")).get("currency")).get("code") != "RUB":
        name = ((transactions.get("operationAmount")).get("currency")).get("code")
        amount = (transactions.get("operationAmount")).get("amount")
        path_env = os.path.join(os.getcwd(), ".env")
        load_dotenv(path_env)
        api_key = os.getenv("API_KEY")
        url = f"https://api.apilayer.com/exchangerates_data/convert?to=RUB&from={name}&amount={amount}"
        payload = {}
        headers= {
          "apikey": f"{api_key}"
        }

        response = requests.request("GET", url, headers=headers, data = payload)

        status_code = response.status_code
        result = response.json()
        return f"{result.get("result"):.2f}"
    else:
        return (transactions.get("operationAmount")).get("amount")


    # print(api_key)
    # return result