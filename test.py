import requests
import json

lat='52.3596222879797'
lon = '4.857487989623271'
api_key = 'e17eea2c80cac604e7664e5842aca1a1'
part = 'minutely,hourly,daily,alerts'

rain = requests.get(f'https://gpsgadget.buienradar.nl/data/raintext?lat={lat}&lon={lon}')
print('rain   ',rain.text[:3])

temp = requests.get(f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={api_key}&units=metric')
print('temp   ',json.loads(temp.text)['current']['temp'])

# print(temp.json())
# 52.3596222879797, 4.857487989623271   j.j. Creperplein
# e17eea2c80cac604e7664e5842aca1a1       api key openwheathemap


# https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
 

