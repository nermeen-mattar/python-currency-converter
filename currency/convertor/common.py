from django.http import JsonResponse
from django.forms.models import model_to_dict
# from .serializer import CurrencySerializer

import requests
import json

def changeFromAlphavantageParams(data):
    price_line = {
        "from_code": data['1. From_Currency Code'],
        "from_name": data['2. From_Currency Name'],
        "to_code": data['3. To_Currency Code'],
        "to_name": data['4. To_Currency Name'],
        "exchange_rate": data['5. Exchange Rate'],
        "last_refreshed": data['6. Last Refreshed'],
        "bid": data['8. Bid Price'],
        "ask": data['9. Ask Price']
    }
    # print(price_line)
    return price_line

def get_currency_exchange():
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=X62XVBHZ07NR9WSL';
    x = requests.get(url, data = {}).json()
    print(x["Realtime Currency Exchange Rate"])
    
    return changeFromAlphavantageParams(x["Realtime Currency Exchange Rate"])
