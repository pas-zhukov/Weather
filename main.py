import requests

url_template = 'https://wttr.in/{}?n&T&m&lang=ru&M&q'

places = ['Лондон', 'Аэропорт Шереметьево', 'Череповец']

for place in places:
  data = requests.get(url_template.format(place))
  print(data.text)

