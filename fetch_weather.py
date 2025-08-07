import weather_api_connection as wac
import sqlite3 as sq

def fetch_weather_for_city(city):
    # this function should return the row to be inserted in the weather table

    # get the raw data
    weather_dict = wac.extract_weather_data(city)
    print(weather_dict)

    #cherry-picking the items we want
    temp = weather_dict['main']['temp']
    humidity = weather_dict['main']['humidity']
    wind_speed = weather_dict['wind']['speed']
    wind_direction = map_wind_direction(weather_dict['wind']['deg'])

    return temp, humidity, wind_speed, wind_direction

def fetch_list_of_cities():
    #connect to database
    conn = sq.connect('weather.db')
    cursor = conn.cursor()

    #fetch cities
    cursor.execute('SELECT id, name FROM city')
    cities = cursor.fetchall()

    #close the connection
    conn.close()

    return cities


def map_wind_direction(wind_direction):
    #this function should switch from degree to direction
    if isinstance(wind_direction,(int, float)) and 0 <= wind_direction <= 360:
        directions = ['North', 'North-East', 'East', 'South-East', 'South', 'South-West', 'West', 'North-West']

        wind_direction = wind_direction + 22.5 #rotating the scale
        wind_direction = wind_direction % 360

        index = int(wind_direction/45)
        return directions[index]
    else:
        return 'Unknown'


if __name__ == '__main__':
   fetch_weather_for_city('London')
