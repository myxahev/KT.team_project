# Модуль получения данных с API и запись в базу данных.

"""
curl -H "X-CMC_PRO_API_KEY: d61bca4c-e9d3-40b9-8d82-abf9b057ffbd"
-H "Accept: application/json" -d "id=1"
-G https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest
"""

import requests

def response():
    return requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest', headers={
        'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd',
        'Accept': 'application/json',
    }, params=(('id', '1'),))



