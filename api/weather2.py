import requests

API_KEY = "9b4fce1f9e03a96e213bcaf94573adde"
CURRENT = "http://api.weatherstack.com/current"
FORECAST = "http://api.weatherstack.com/forecast"

def get_current_weather():
    payload = {"access_key":API_KEY, "query": "Budapest", "forecast_days":2, "hourly":3}
    r = requests.get(CURRENT, params=payload)
    fc = r.json()
    print(fc)

get_current_weather()