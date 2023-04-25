import requests

url_template = 'https://wttr.in/{}'

places = ['Лондон', 'Аэропорт Шереметьево', 'Череповец']

params = {
    'n': '',
    'T': '',
    'm': '',
    'M': '',
    'q': '',
    'lang': 'ru'
}

for place in places:
    response = requests.get(url_template.format(place), params=params)
    response.raise_for_status()  # Поднимет исключение в случае ответа с кодом типа 4XX или 5ХХ
    print(response.text)
