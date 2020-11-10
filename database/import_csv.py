import pandas as pd
import numpy as np
import pymysql
import datetime

airlines = pd.read_csv("data-csv/airlines.csv",
                       sep=',').replace(r'^\s*$', "NULL", regex=True)
airports = pd.read_csv("data-csv/airports.csv",
                       sep=',').replace(r'^\s*$', "NULL", regex=True)
planes = pd.read_csv("data-csv/planes.csv",
                     sep=',').replace(r'^\s*$', "NULL", regex=True)
weather = pd.read_csv("data-csv/weather.csv",
                      sep=',').replace(r'^\s*$', "NULL", regex=True)
flights = pd.read_csv("data-csv/flights.csv",
                      sep=',').replace(r'^\s*$', "NULL", regex=True)

# HOST: db4free.net
# USERNAME: ingrdb
# PASSWORD: db4freeIngr
# DATABASE: airtrafficdb


# database config
HOST = "localhost"
USERNAME = "rbtkay"
PASSWORD = "password"
DATABASE = "airtraffic"

format = '%Y-%m-%dT%H:%M:%S%z'


db = pymysql.connect(HOST, USERNAME, PASSWORD, DATABASE)

cursor = db.cursor()

# for index, row in airlines.iterrows():
#     try:
#         sql_query = "INSERT INTO airlines (carrier, name) VALUES (%s, %s)"
#         val = (row['carrier'], row['name'])
#         cursor.execute(sql_query, val)

#         db.commit()
#     except Exception as e:
#         print(e)
#         print(f"Error: unable to insert {row['carrier']}")

# print("INSERT DONE FOR AIRLINES!")

# for index, row in airports.iterrows():
#     try:
#         sql_query = "INSERT INTO airports (faa,name,lat,lon,alt,tz,dst,tzone) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
#         val = (row['faa'], row['name'], row['lat'], row['lon'],
#                row['alt'], row['tz'], row['dst'], row['tzone'])
#         cursor.execute(sql_query, val)

#         db.commit()
#     except Exception as e:
#         print(e)
#         print(f"Error: unable to insert {row['faa']}")

# print("INSERT DONE FOR AIRPORTS!")

# for index, row in planes.iterrows():
#     try:
#         sql_query = "INSERT INTO planes (tailnum, year, type, manufacturer, model, engines, seats, speed, engine) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"

#         year = row['year']
#         speed = row['speed']

#         if row['year'] == "NULL":
#             year = None
#         if row['speed'] == "NULL":
#             speed = None

#         val = (row['tailnum'], year, row['type'], row['manufacturer'],
#                row['model'], row['engines'], row['seats'], speed, row['engine'])
#         cursor.execute(sql_query, val)

#         db.commit()
#     except Exception as e:
#         print(e)
#         print(f"Error: unable to insert {row['tailnum']}")

# print("INSERT DONE FOR PLANES!")

# for index, row in weather.iterrows():

#     try:
#         origin = None if row['origin'] == "NULL" else row['origin']
#         year = None if row['year'] == "NULL" else row['year']
#         month = None if row['month'] == "NULL" else row['month']
#         day = None if row['day'] == "NULL" else row['day']
#         hour = None if row['hour'] == "NULL" else row['hour']
#         temp = None if row['temp'] == "NULL" else row['temp']
#         dewp = None if row['dewp'] == "NULL" else row['dewp']
#         humid = None if row['humid'] == "NULL" else row['humid']
#         wind_dir = None if row['wind_dir'] == "NULL" else row['wind_dir']
#         wind_speed = None if row['wind_speed'] == "NULL" else row['wind_speed']
#         wind_gust = None if row['wind_gust'] == "NULL" else row['wind_gust']
#         precip = None if row['precip'] == "NULL" else row['precip']
#         pressure = None if row['pressure'] == "NULL" else row['pressure']
#         visib = None if row['visib'] == "NULL" else row['visib']
#         time_hour = None if row['time_hour'] == "NULL" else datetime.datetime.strptime(
#             row['time_hour'], format)

#         sql_query = "INSERT INTO weather (origin,year,month,day,hour,temp,dewp,humid,wind_dir,wind_speed,wind_gust,precip,pressure,visib,time_hour) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
#         val = (origin, year, month, day, hour, temp, dewp, humid,
#                wind_dir, wind_speed, wind_gust, precip, pressure, visib, time_hour)

#         cursor.execute(sql_query, val)
#         db.commit()
#     except Exception as e:
#         print(e)
#         print(f"Error: unable to insert {row['origin']}")

# print("INSERT DONE FOR WEATHER!")


for index, row in flights.iterrows():
    try:
        year = None if row["year"] == "NULL" else row["year"]
        month = None if row["month"] == "NULL" else row["month"]
        day = None if row["day"] == "NULL" else row["day"]
        dep_time = None if row["dep_time"] == "NULL" else row["dep_time"]
        arr_time = None if row["arr_time"] == "NULL" else row["arr_time"]
        sched_dep_time = None if row["sched_dep_time"] == "NULL" else row["sched_dep_time"]
        sched_arr_time = None if row["sched_arr_time"] == "NULL" else row["sched_arr_time"]
        dep_delay = None if row["dep_delay"] == "NULL" else row["dep_delay"]
        arr_delay = None if row["arr_delay"] == "NULL" else row["arr_delay"]
        hour = None if row["hour"] == "NULL" else row["hour"]
        minute = None if row["minute"] == "NULL" else row["minute"]
        carrier = None if row["carrier"] == "NULL" else row["carrier"]
        tailnum = None if row["tailnum"] == "NULL" else row["tailnum"]
        flight = None if row["flight"] == "NULL" else row["flight"]
        origin = None if row["origin"] == "NULL" else row["origin"]
        dest = None if row["dest"] == "NULL" else row["dest"]
        distance = None if row["distance"] == "NULL" else row["distance"]
        air_time = None if row["air_time"] == "NULL" else row["air_time"]
        time_hour = None if row["time_hour"] == "NULL" else datetime.datetime.strptime(
            row["time_hour"], format)

        sql_query = "INSERT INTO flights (year, month, day, dep_time, sched_dep_time, dep_delay, arr_time, sched_arr_time, arr_delay, carrier, flight, tailnum, origin, destination, air_time, distance, hour, minute, time_hour) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (year, month, day, dep_time, sched_dep_time, dep_delay, arr_time, sched_arr_time, arr_delay, carrier, flight, tailnum, origin, dest, air_time, distance, hour, minute, time_hour)

        cursor.execute(sql_query, val)
        db.commit()
    except Exception as e:
        print(e)
        print(f"Error: unable to insert {row['origin']}")


print("INSERT DONE FOR FLIGHTS!")

db.close()


# print(airlines)
# print(airports)
# print(planes)
# print(weather)
# print(flights)
