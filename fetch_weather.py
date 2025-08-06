from pandas.core.computation.ops import isnumeric

import weather_api_connection as wac


def fetch_weather_for_city(city):
    # this function should return the row to be inserted in the weather table

    # get the raw data
    raw_data_for_city = wac.extract_weather_data(city)
    print(raw_data_for_city)

# let's extract what we need

# date TEXT, temperature NUMERIC, humidity NUMERIC, wind_speed NUMERIC, wind_direction NUMERIC,

def map_wind_direction(wind_direction):
    #this function should switch from degree to direction
    if isnumeric(wind_direction):
        directions = ['North', 'North-East', 'East', 'South-East', 'South', 'South-West', 'West', 'North-West']

        wind_direction = wind_direction + 360/len(directions) #rotating the scale

        i = int(wind_direction/45) % 8
        return directions[i]
    else:
        return 'North'


if __name__ == '__main__':
 #   fetch_weather_for_city('London')

    print(map_wind_direction(230))
    print(map_wind_direction(1))
    print(map_wind_direction(350))
    print(map_wind_direction(22.5))