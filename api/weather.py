import requests
from pprint import pprint

API_KEY = "9d39043234930007b2bd308ab2da17b8"
API_URL = "https://api.openweathermap.org/data/2.5/weather"
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

def main():
    lat, lon = get_coords(2094, "HU")
    weather = get_weather(lat, lon)
    pprint(weather)

main()