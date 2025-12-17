import requests
from .config import get_settings

settings = get_settings()

def get_weather_data(location: str, start_date: str, end_date: str):
    base_url = settings.api_base_url
    api_url = f'{base_url}/{location}/{start_date}/{end_date}'
    parameters = {
        'key': settings.weather_api_key
    }
    response = requests.get(api_url, params=parameters)
    data = response.json()
    return data
