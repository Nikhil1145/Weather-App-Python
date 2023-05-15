import requests
from dotenv import load_dotenv
import os
from dataclasses import dataclass

load_dotenv()
api_key = os.getenv('API_KEY')

@dataclass
class WeatherData:
    main:str
    description:str
    icon:str
    temperature:float



def get_lat_lon(city_name, state_code, country_code, API_key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city_name},{state_code},{country_code}&appid={API_key}').json()

    lat, lon = resp['coord']['lat'], resp['coord']['lon']
    return lat, lon

def get_current_weather(lat , lon , API_Key):
    resp = requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_Key}&units=metric').json()
    print(resp)
    
    data=WeatherData(
        main = resp.get('weather')[0].get('main'),
        description=resp.get('weather')[0].get('description'),
        icon=resp.get('weather')[0].get('icon'),
        temperature=resp.get('main').get('temp'),
    )
    return data

def main(city_name , state_name , country_name):
    lat , lon = get_lat_lon(city_name , state_name , country_name, api_key)
    weatherData = get_current_weather(lat , lon , api_key)
    return weatherData

if __name__ == "__main__":
    lat , lon = get_lat_lon('Jaipur', 'RJ', 'India', api_key)
    print(get_current_weather(lat , lon , api_key))
 

