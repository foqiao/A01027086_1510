import requests
import json


def get_forecast(url: str) -> None:
    response = requests.get(url)
    response.raise_for_status()
    vancouver_weather = json.loads(response.text)
    # print(vancouver_weather)
    w = vancouver_weather['list']
    print('Current weather in Vancouver:')
    print(w[0]['weather'][0]['main'], '-', w[0]['weather'][0]['description'])
    print()
    print('Tomorrow:')
    print(w[1]['weather'][0]['main'], '-', w[1]['weather'][0]['description'])
    print()
    print('Day after tomorrow:')
    print(w[2]['weather'][0]['main'], '-', w[2]['weather'][0]['description'])


def main():
    vancouver = 6173331
    api_key = "73e6dd36a2a073c414a629760ac198ce"
    url = "http://api.openweathermap.org/data/2.5/forecast?id=6173331&APPID=73e6dd36a2a073c414a629760ac198ce"
    get_forecast(url)

if __name__ == '__main__':
    main()