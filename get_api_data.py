from dotenv import load_dotenv
from pathlib import Path
import os
import requests
import pandas as pd

dotenv_path = Path('../.env')

load_dotenv(dotenv_path=dotenv_path)
OPENWEATHER_API_KEY = os.getenv('OPENWEATHER_API_KEY')

url = "https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}".format(
    city='paris',
    api_key=OPENWEATHER_API_KEY
)


r = requests.get(url)
print(pd.read_json(url))
