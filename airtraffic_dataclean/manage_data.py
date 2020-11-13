import pandas as pd
import sqlalchemy
import datetime
from env import DATABASE

engine = sqlalchemy.create_engine(DATABASE)


def void_to_null(df):
    return df.replace(r'^\s*$', "NULL", regex=True)


def clean_and_insert_data():
    airlines = void_to_null(pd.read_csv("data-csv/airlines.csv"))
    airports = void_to_null(pd.read_csv("data-csv/airports.csv"))
    flights = void_to_null(pd.read_csv("data-csv/flights.csv"))
    planes = void_to_null(pd.read_csv("data-csv/planes.csv"))
    weather = void_to_null(pd.read_csv("data-csv/weather.csv"))

    format = '%Y-%m-%dT%H:%M:%S%z'

    def check_if_null(s): return s if s != "NULL" else None
    def check_primary_if_null(s): return s if s != "NULL" else "Unknown"

    def check_time_if_null(s):
        return datetime.datetime.strptime(s, format) if s != "NULL" else None

    MISSING_AIRPORTS = pd.DataFrame({
        "faa": ['BQN', 'PSE', 'SJU', 'STT'],
        "name": ['Rafael Hernandez Airport', 'Mercedita Airport', 'San Juan Airport', 'Cyril E. King Airport'],
        "lat": ["NULL", "NULL", "NULL", "NULL"],
        "lon": ["NULL", "NULL", "NULL", "NULL"],
        "alt": ["NULL", "NULL", "NULL", "NULL"],
        "tz": ["NULL", "NULL", "NULL", "NULL"],
        "dst": ["NULL", "NULL", "NULL", "NULL"],
        "tzone": ["NULL", "NULL", "NULL", "NULL"]
    })

    airports = pd.concat([airports, MISSING_AIRPORTS])

    flights_serie = flights["tailnum"].unique()
    planes_serie = planes["tailnum"]

    # get the missing planes
    missing_planes = set(flights_serie) - set(planes_serie)
    missing_planes.remove("NULL")

    missing_planes = pd.DataFrame({
        "tailnum": [plane for plane in missing_planes],
        "year": ["NULL" for _ in missing_planes],
        "type": ["NULL" for _ in missing_planes],
        "manufacturer": ["NULL" for _ in missing_planes],
        "model": ["NULL" for _ in missing_planes],
        "engines": ["NULL" for _ in missing_planes],
        "seats": ["NULL" for _ in missing_planes],
        "speed": ["NULL" for _ in missing_planes],
        "engine": ["NULL" for _ in missing_planes]
    })

    # add the missing plane to the dataframe
    planes = pd.concat([planes, missing_planes])

    airlines = pd.DataFrame({
        "carrier": [check_primary_if_null(a) for a in airlines["carrier"]],
        "name": [check_if_null(a) for a in airlines["name"]],
    })

    planes = pd.DataFrame({
        "tailnum": [check_primary_if_null(t) for t in planes["tailnum"]],
        "year": [check_if_null(t) for t in planes["year"]],
        "type": [check_if_null(t) for t in planes["type"]],
        "manufacturer": [check_if_null(t) for t in planes["manufacturer"]],
        "model": [check_if_null(t) for t in planes["model"]],
        "engines": [check_if_null(t) for t in planes["engines"]],
        "seats": [check_if_null(t) for t in planes["seats"]],
        "speed": [check_if_null(t) for t in planes["speed"]],
        "engine": [check_if_null(t) for t in planes["engine"]]
    })

    airports = pd.DataFrame({
        "faa": [check_primary_if_null(airport) for airport in airports["faa"]],
        "name": [check_if_null(airport) for airport in airports["name"]],
        "lat": [check_if_null(airport) for airport in airports["lat"]],
        "lon": [check_if_null(airport) for airport in airports["lon"]],
        "alt": [check_if_null(airport) for airport in airports["alt"]],
        "tz": [check_if_null(airport) for airport in airports["tz"]],
        "dst": [check_if_null(airport) for airport in airports["dst"]],
        "tzone": [check_if_null(airport) for airport in airports["tzone"]]
    })

    weather = pd.DataFrame({
        "origin": [check_primary_if_null(w) for w in weather["origin"]],
        "year": [check_if_null(w) for w in weather["year"]],
        "month": [check_if_null(w) for w in weather["month"]],
        "day": [check_if_null(w) for w in weather["day"]],
        "hour": [check_if_null(w) for w in weather["hour"]],
        "temp": [check_if_null(w) for w in weather["temp"]],
        "dewp": [check_if_null(w) for w in weather["dewp"]],
        "humid": [check_if_null(w) for w in weather["humid"]],
        "wind_dir": [check_if_null(w) for w in weather["wind_dir"]],
        "wind_speed": [check_if_null(w) for w in weather["wind_speed"]],
        "wind_gust": [check_if_null(w) for w in weather["wind_gust"]],
        "precip": [check_if_null(w) for w in weather["precip"]],
        "pressure": [check_if_null(w) for w in weather["pressure"]],
        "visib": [check_if_null(w) for w in weather["visib"]],
        "time_hour": [check_time_if_null(w) for w in weather["time_hour"]]
    })

    flights = pd.DataFrame({
        "year": [check_if_null(f) for f in flights["year"]],
        "month": [check_if_null(f) for f in flights["month"]],
        "day": [check_if_null(f) for f in flights["day"]],
        "dep_time": [check_if_null(f) for f in flights["dep_time"]],
        "sched_dep_time": [check_if_null(f) for f in flights["sched_dep_time"]],
        "dep_delay": [check_if_null(f) for f in flights["dep_delay"]],
        "arr_time": [check_if_null(f) for f in flights["arr_time"]],
        "sched_arr_time": [check_if_null(f) for f in flights["sched_arr_time"]],
        "arr_delay": [check_if_null(f) for f in flights["arr_delay"]],
        "carrier": [check_if_null(f) for f in flights["carrier"]],
        "flight": [check_if_null(f) for f in flights["flight"]],
        "tailnum": [check_if_null(f) for f in flights["tailnum"]],
        "origin": [check_if_null(f) for f in flights["origin"]],
        "dest": [check_if_null(f) for f in flights["dest"]],
        "air_time": [check_if_null(f) for f in flights["air_time"]],
        "distance": [check_if_null(f) for f in flights["distance"]],
        "hour": [check_if_null(f) for f in flights["hour"]],
        "minute": [check_if_null(f) for f in flights["minute"]],
        "time_hour": [check_time_if_null(f) for f in flights["time_hour"]]
    })

    airlines.to_sql('airline', con=engine, if_exists='append', index=False)
    airports.to_sql('airport', con=engine, if_exists='append', index=False)
    planes.to_sql('plane', con=engine, if_exists='append', index=False)
    weather.to_sql('weather', con=engine, if_exists='append', index=False)
    flights.to_sql('flight', con=engine, if_exists='append', index=False)
