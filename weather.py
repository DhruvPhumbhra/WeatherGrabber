import requests
import json
import os

OWM_BASE = 'http://api.openweathermap.org/data/2.5/weather'
OWM_API_KEY = os.environ.get('OWM_API_KEY')

def get_city_temp(city):
    response = requests.get(
        OWM_BASE,
        params={
            'q': city,
            'units': 'Imperial',
            'APPID': OWM_API_KEY
        }
    )
    return get_temp(response)


def get_temp(response):
    obj = json.loads(response.text)
    if response.status_code == 200:
        return round(obj['main']['temp'])
    raise Exception('ERROR {0} {1}'.format(
            response.status_code,
            obj['message']
        )
    )


if __name__ == '__main__':
    city = raw_input('Where are you? ')
    city_arr = city.split()
    if len(city_arr[-1]) == 2:
        del city_arr[-1]
    city = " ".join(city_arr)
    temp = get_city_temp(city);
    
    print('{0} Weather:\n{1} degrees Fahrenheit'.format(
            city, temp
        )
    )

