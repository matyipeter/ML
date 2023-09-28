import requests
from pprint import pprint

API_KEY = "9d39043234930007b2bd308ab2da17b8"
API_URL = "https://api.openweathermap.org/data/2.5/forecast"
GEO_API_URL = "http://api.openweathermap.org/geo/1.0/zip"

def get_coords(zip, cc):
    payload = {'zip':str(zip)+','+cc, 'appid':API_KEY}
    location = requests.get(GEO_API_URL, params=payload)
    lat, lon = location.json()["lat"], location.json()['lon']
    return lat, lon

def get_weather(lat, lon):
    payload = {"lat":lat, "lon": lon,'units': 'metric','lang': 'hu' ,'appid': API_KEY}
    weather = requests.get(API_URL, params=payload)
    data = weather.json()
    return data

def day_temp(data):
    days = data["list"]
    day_temp = {}
    for i in days:
        if i['dt_txt'][8:10] in day_temp:
            day_temp[i['dt_txt'][8:10]].append(i['main']['temp'])
        else:
            day_temp[i['dt_txt'][8:10]] = []
            day_temp[i['dt_txt'][8:10]].append(i['main']['temp'])
    
    day_max = {}
    for i in day_temp:
        day_max[i] = max(day_temp[i])

    return day_max


def main():
    lat, lon = get_coords(2094, "HU")
    weather = get_weather(lat, lon)
    temps = day_temp(weather)
    for i in temps:
        print(f'{i}. {temps[i]} fok lesz a maximum')

main()