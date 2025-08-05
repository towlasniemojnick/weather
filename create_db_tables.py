import sqlite3

cursor = sqlite3.connect('weather.db')

cursor.execute("""
    CREATE TABLE city (
	id	INTEGER,
	name	TEXT UNIQUE,
	country	TEXT,
	PRIMARY KEY(id AUTOINCREMENT)
	)
    """)

cursor.execute("""
    CREATE TABLE weather(
               id INTEGER,
               city_id INTEGER,
               date TEXT,
               temperature NUMERIC,
               humidity NUMERIC,
               wind_speed NUMERIC,
               wind_direction NUMERIC,
               PRIMARY KEY(id AUTOINCREMENT),
               FOREIGN KEY (city_id) REFERENCES city(id)
    )
    """)

cursor.commit()
cursor.close()
