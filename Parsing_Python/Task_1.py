import requests

city_id = int(input())  # 498817 для Санкт-Петербурга
appid = input()

try:
    res = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'id': city_id, 'units': 'metric', 'APPID': appid})
    data = res.json()
    MAX_hpa = float('-inf')
    for i in data['list']:
        if MAX_hpa < i['main']['pressure']:
            MAX_hpa = i['main']['pressure']
    print('В этот день и время:',i['dt_txt'], 'будет максимальное давление в ближайшие пять дней, которое равняется',MAX_hpa,'hpa')
except Exception as e:
    print("Exception (forecast):", e)
