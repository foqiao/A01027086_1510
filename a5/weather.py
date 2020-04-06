import json

import openweather
from datetime import datetime

import requests

def api(day):
   for i in range(1, int(day) + 1):
        url = 'https://api.openweathermap.org/data/2.5/weather?q=Vancouver&cnt=%d&appid=d8ecf789b325a' \
              '7d40e4c0b03c57ff60d' % i
        weather_API = requests.get(url)
        json_converter = json.loads(weather_API.text)

        # create client
        ow = openweather.OpenWeather()

        # historic weather
        start_date = datetime(json_converter['cnt'])
        end_date = datetime(json_converter['cnt'])
        dt = datetime(json_converter.list[0]['dt'])
        sunrise = datetime(json_converter.list[0]['sunrise'])
        sunset = datetime(json_converter.list[0]['sunset'])
        city_id = api.list.city.id
        # default: hourly interval
        print(ow.get_historic_weather(city_id, start_date, end_date))

        # daily aggregates
        print(ow.get_historic_weather(city_id, start_date, end_date, "day"))

def weather_vancouver(i, json_converter):
    w = json_converter['list']
    print('Day: %d' % i)
    print(f'humidity: {json_converter.list.humidity}')
    print(f'sunrise: {sunrise}')
    print(f'sunset: {sunset}')
    print(f'daytime: {dt}')

def main():
    day = input("How many days do you want: ")
    api(day)

if __name__ == '__main__':
    main()