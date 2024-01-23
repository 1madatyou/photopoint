import json

import requests 

from core.settings import APILAYER_API_KEY 
from .models import CurrencyRate


def get_currency(from_currency: str, to_currency: str):
    '''Get currency rate by passed currencies'''
    url = f"https://api.apilayer.com/exchangerates_data/latest?symbols={to_currency}&base={from_currency}"

    payload = {}
    headers= {
    "apikey": "9UpLGZA88rzvuAwtQPk5pudgj0bz1ikM"
    }

    response = requests.request("GET", url, headers=headers, data = payload)
    response_body = json.loads(response.content)

    rate = response_body['rates'].get(to_currency)

    CurrencyRate.objects.create(
        from_currency=from_currency,
        to_currency=to_currency,
        rate=rate
    )
