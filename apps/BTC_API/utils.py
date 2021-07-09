# Модуль получения данных с API и запись в базу данных.

"""
curl -H "X-CMC_PRO_API_KEY: d61bca4c-e9d3-40b9-8d82-abf9b057ffbd"
-H "Accept: application/json" -d "id=1"
-G https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest
"""

import requests

def response():
    response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest', headers={
        'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd',
        'Accept': 'application/json',
    }, params=(('id', '1'),))
    data = response.json()
    array = []
    array.append(data['data']['1']['name'])
    array.append(data['data']['1']["date_added"])
    array.append(data['data']['1']["last_updated"])
    array.append(data['data']['1']["quote"]["USD"]["price"])
    array.append(data['data']['1']["quote"]["USD"]["volume_24h"])
    array.append(data['data']['1']["quote"]["USD"]["percent_change_24h"])
    return array

print(response())

"""response = requests.get('https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest', headers={
        'X-CMC_PRO_API_KEY': 'd61bca4c-e9d3-40b9-8d82-abf9b057ffbd',
        'Accept': 'application/json',
    }, params=(('id', '1'),))
print("response.text:\n{}\n\n".format(response.text))
data = response.json()
print(data['data']['1']['name'])
print(data['data']['1']["date_added"])
print(data['data']['1']["last_updated"])
print(data['data']['1']["quote"]["USD"]["price"])
print(data['data']['1']["quote"]["USD"]["volume_24h"])
print(data['data']['1']["quote"]["USD"]["percent_change_24h"])"""

print(response())