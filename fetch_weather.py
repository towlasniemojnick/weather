import weather_api_connection as wac
import sqlite3 as sq
import datetime


def fetch_weather_for_city(id,city):
    # this function should return the row to be inserted in the weather table

    # get the raw data
    weather_dict = wac.extract_weather_data(city)

    #cherry-picking the items we want
    temp = weather_dict['main']['temp']
    humidity = weather_dict['main']['humidity']
    wind_speed = weather_dict['wind']['speed']
    wind_direction = map_wind_direction(weather_dict['wind']['deg'])
    today = datetime.date.today()

    return id,today,temp, humidity, wind_speed, wind_direction

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

def get_weather_for_all_cities():

    cities = fetch_list_of_cities()
    weather_list = []

    for city in cities:
        weather_list.append(fetch_weather_for_city(city[0],city[1]))

    print(weather_list)

    conn = sq.connect('weather.db')
    cursor = conn.cursor()

    cursor.executemany('INSERT INTO weather(city_id, date, temperature, humidity, wind_speed, wind_direction) VALUES(?,?,?,?,?,?)',weather_list)
    conn.commit()
    conn.close()

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
    get_weather_for_all_cities()
