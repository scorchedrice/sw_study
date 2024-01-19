
import requests
import pprint

lat = 37.56
lon = 126.97
api_key = '096f144c53a055708d4086931dd74306'
url = f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}'

data = requests.get(url).json()
pprint.pprint(data.get('weather')[0].get('description'))

# data.get('weather'), data['weather'] 무슨차이???

'''
PJT1-1
python 정기예금 데이터 수집 및 미션 수행

'''