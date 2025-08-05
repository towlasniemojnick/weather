import os
import requests
from dotenv import load_dotenv

def get_the_key():
    load_dotenv()
    api_key = os.getenv('WEATHER_API_KEY')
    return api_key

def extract_weather_data(api_key, city):
    print("Trying to get data from OpenWeatherMap...")

    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    req = requests.get(api_url)
    req.raise_for_status()

    data = req.json()

    print(data)

if __name__ == "__main__":
    extract_weather_data(get_the_key(), "Warsaw")