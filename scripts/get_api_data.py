import sys
sys.path.append('/app/')
from dotenv import load_dotenv
import os
import requests
import pandas as pd
from airflow.models import Variable
import json

from utils.JsonClassUtils import JsonClassUtils

load_dotenv()
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')

Variable.set(key="cities", value=json.dumps(['paris', 'london', 'washington']))


def get_weather_data():
    cities = Variable.get(key="cities", deserialize_json=True)

    url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    dts = []
    res_list = []
    for city in cities:
        url_city = url.format(city=city, api_key=WEATHER_API_KEY)
        r_json = requests.get(url_city).json()
        print(r_json)
        res_list.append(r_json)
        dts.append(r_json['dt'])

    times = pd.to_datetime(dts, unit='s').strftime('%Y-%m-%d %H:%M')
    print(times)
    time = max(times)
    print(time)

    JsonClassUtils().write_obj_json('/app/raw_files/%s.json' % time, res_list)
