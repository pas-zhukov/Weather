import requests

url_template = 'https://wttr.in/{}'

locations = ['Лондон', 'Аэропорт Шереметьево', 'Череповец']

params = {
    'n': '',
    'T': '',
    'm': '',
    'M': '',
    'q': '',
    'lang': 'ru'
}

for location in locations:
    response = requests.get(url_template.format(location), params=params)
    response.raise_for_status()  # Поднимет исключение в случае ответа с кодом типа 4XX или 5ХХ
    print(response.text)
