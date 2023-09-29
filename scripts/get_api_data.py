from dotenv import load_dotenv
import os
import requests
import pandas as pd
# from airflow.models import Variable
from pathlib import Path

from utils.JsonClassUtils import JsonClassUtils

dotenv_path = Path('./.env')
load_dotenv(dotenv_path=dotenv_path)
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

cities = ['paris', 'london', 'washington']


def get_weather_data():

    url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    dt = None
    res_list = []
    for city in cities:
        url_city = url.format(city=city, api_key=WEATHER_API_KEY)
        r_json = requests.get(url_city).json()
        res_list.append(r_json)
        dt = r_json['dt']

    time = pd.to_datetime(dt, unit='s').strftime('%Y-%m-%d %H:%M')

    JsonClassUtils().write_obj_json('./raw_files/%s.json' % time, res_list)


get_weather_data()
