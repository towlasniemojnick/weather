import weather_api_connection as wac
import sqlite3 as sq

def fetch_weather_for_city(city):
    # this function should return the row to be inserted in the weather table

    # get the raw data
    raw_data_for_city = wac.extract_weather_data(city)
    print(raw_data_for_city)

# let's extract what we need

# date TEXT, temperature NUMERIC, humidity NUMERIC, wind_speed NUMERIC, wind_direction NUMERIC,

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
 #   fetch_weather_for_city('London')
    print(fetch_list_of_cities())