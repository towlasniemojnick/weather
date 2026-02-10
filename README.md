# Weather

A small Python tool to fetch current weather data via OpenWeather API and store it in an SQLite database.

## Features
- **Fetch:** Automated weather retrieval (temp, wind, humidity).
- **Transform:** Wind direction conversion from degrees to cardinal points.
- **Store:** Persistent storage using SQLite.
- **Secure:** Environment variable management for API keys.

## Quick Start

1. **Environment:**
   ```bash
   pip install -r requirements.txt
   
2. **API:**
- Register on OpenWeather.
- Generate your own API key.
- Store it in the .env file, you can get inspiration from .env.example
- **Do not add. .env file to git**

3. **Project structure:**

- create_db_tables.py - to create db schema
- insert_initial_cities.py - to insert cities (examples)
- fetch_weather.py - main logic of the tool
- weather_api_connection.py - connection to OpenWeather
- test_wind_direction.py - test for function logic