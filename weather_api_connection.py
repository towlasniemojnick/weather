import os
import requests
from dotenv import load_dotenv

def get_the_key():
    #load the api key
    load_dotenv()
    api_key = os.getenv('WEATHER_API_KEY')
    return api_key

def extract_weather_data(city):
    print("Trying to get data from OpenWeatherMap...")
    api_key = get_the_key()

    #formulate the url string
    api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    #trying to get the response
    try:
        req = requests.get(api_url)
        req.raise_for_status()

        data = req.json()
        print(f"Data fetched from OpenWeatherMap for {city}")

        #return data as is
        return(data)

    #handle the exception - not providing the full description, as this may reveal the API key in some case
    except requests.exceptions.HTTPError as err:

        error_response = err.response
        status_code = error_response.status_code
        reason = error_response.reason

        print(f"Error: {status_code} - {reason}")

    except requests.exceptions.RequestException as err:

        print(f"Error: Could not fetch data from OpenWeatherMap for {city}. Check connection or API key and try again.")

if __name__ == "__main__":
    city_data = extract_weather_data("Miedzyzdroje")

    print(city_data)