import requests
from .config import get_settings
import datetime as dt

settings = get_settings()

def get_weather_data(location: str, start_date: str, end_date: str):

    if start_date is None or not len(start_date):
        start_date = dt.date.today().strftime('%Y-%m-%d')
    if end_date is None or not len(end_date):
        end_date = dt.date.today().strftime('%Y-%m-%d')


    if start_date is not None:
        start_date = start_date.replace('/','-')
    if end_date is not None:
        end_date = end_date.replace('/', '-')

    base_url = settings.api_base_url
    api_url = f'{base_url}/{location}/{start_date}/{end_date}'
    parameters = {
        'key': settings.weather_api_key
    }
    response = requests.get(api_url, params=parameters)
    # print(response.content)
    data = response.json()
    return data
