import sqlite3

#creating the connection to the database
cursor = sqlite3.connect('weather.db')

#creating dimension table for cities
cursor.execute("""INSERT INTO city (name, country) VALUES ('Miedzyzdroje', 'PL');""")
cursor.execute("""INSERT INTO city (name, country) VALUES ('Warsaw', 'PL');""")
cursor.execute("""INSERT INTO city (name, country) VALUES ('London', 'EN');""")

cursor.commit()
cursor.close()
