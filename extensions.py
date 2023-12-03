import requests
import json
from config import keys


class APIExeption(Exception):
    pass


class CryptoConverter:
    @staticmethod
    def get_price(quote: str, base: str, amount: str):

        if quote == base:
            raise APIExeption(f'Невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIExeption(f'Не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIExeption(f'Не удалось обработать колличество {amount}')

        r = requests.get(f'https://v6.exchangerate-api.com/v6/ef0e936bfb3a7ed11a14b907/pair/{quote_ticker}/{base_ticker}/{amount}')
        data = json.loads(r.content)
        total_base = data.get('conversion_result')

        return total_base

