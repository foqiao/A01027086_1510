import requests
import json
from datetime import datetime


def get_forecast(url: str, day: int) -> None:
    response = requests.get(url)
    response.raise_for_status()
    vancouver_weather = json.loads(response.text)
    for i in range(1, int(day) + 1):
        print(f"Day {i}")
        dt = datetime.fromtimestamp(vancouver_weather['dt'])
        sunrise = datetime.fromtimestamp(vancouver_weather['sys']['sunrise'])
        sunset = datetime.fromtimestamp(vancouver_weather['sys']['sunset'])
        print(f"daytime: {dt}")
        print(f"sunrise: {sunrise}")
        print(f"sunset: {sunset}")
        print(f"temperature: {vancouver_weather['main']['temp']} C")
        print(f"maximum temperature: {vancouver_weather['main']['temp_max']} C")
        print(f"minimum temperature: {vancouver_weather['main']['temp_min']} C")
        print(f"feel_like: {vancouver_weather['main']['feels_like']} C")

def main():
    day = input('How many days do you want to enter: ')
    vancouver = 6173331
    api_key = "f804cceef146b504a64c9d9269f6ee3b"
    url = "http://api.openweathermap.org/data/2.5/weather?q=Vancouver&appid=f804cceef146b504a64c9d9269f6ee3b"
    get_forecast(url, day)

if __name__ == '__main__':
    main()