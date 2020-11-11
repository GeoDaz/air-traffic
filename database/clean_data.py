import pandas as pd

airlines = pd.read_csv("data-csv/airlines.csv").replace(r'^\s*$', "NULL", regex=True)
airports = pd.read_csv("data-csv/airports.csv").replace(r'^\s*$', "NULL", regex=True)
flights = pd.read_csv("data-csv/flights.csv").replace(r'^\s*$', "NULL", regex=True)
planes = pd.read_csv("data-csv/planes.csv").replace(r'^\s*$', "NULL", regex=True)
weather = pd.read_csv("data-csv/weather.csv").replace(r'^\s*$', "NULL", regex=True)


MISSING_AIRPORTS = pd.DataFrame({
    "faa": ['BQN', 'PSE', 'SJU', 'STT'],
    "name": ['Rafael Hernandez Airport', 'Mercedita Airport', 'San Juan Airport', 'Cyril E. King Airport'],
    "lat": ["NULL", "NULL", "NULL", "NULL"],
    "lon": ["NULL","NULL","NULL","NULL"],
    "alt":["NULL","NULL","NULL","NULL"],
    "tz":["NULL","NULL","NULL","NULL"],
    "dst":["NULL","NULL","NULL","NULL"],
    "tzone":["NULL","NULL","NULL","NULL"]
})

airports = pd.concat([airports, MISSING_AIRPORTS])

flights_serie = flights["tailnum"].unique()
planes_serie = planes["tailnum"]

# get the missing planes
missing_planes = set(flights_serie)-set(planes_serie)

# prepare the new planes
planes_to_add = {
    "tailnum": [],
    "year": [],
    "type": [],
    "manufacturer":[],
    "model":[],
    "engines":[],
    "seats":[],
    "speed":[],
    "engine":[]
}

for plane in missing_planes:
    if plane != "NULL": 
        planes_to_add["tailnum"].append(plane)
        planes_to_add["year"].append("NULL")
        planes_to_add["type"].append("NULL")
        planes_to_add["manufacturer"].append("NULL")
        planes_to_add["model"].append("NULL")
        planes_to_add["engines"].append("NULL")
        planes_to_add["seats"].append("NULL")
        planes_to_add["speed"].append("NULL")
        planes_to_add["engine"].append("NULL")


# convert the new planes to a dataframe and add it to the initial one
planes_to_add_df = pd.DataFrame(planes_to_add)

planes = pd.concat([planes, planes_to_add_df])

# print(len(set(flights['dest'].unique()) - set(airports['faa'])))
# print(set(airports['faa']))


# print (set(flights['tailnum'].unique()) - set(planes['tailnum']) == set("NULL"))


if len(set(flights['origin'].unique()) - set(airports['faa'])) > 0:
    print("data is not clean yet... Error on: len(set(flights['origin'].unique()) - set(airports['faa']))")
    exit()
if len(set(flights['dest'].unique()) - set(airports['faa'])):
    print("data is not clean yet... Error on: len(set(flights['dest'].unique()) - set(airports['faa']))")
    exit()
if len(set(weather['origin']) - set(airports['faa'])):
    print("data is not clean yet... Error on: len(set(weather['origin']) - set(airports['faa']))")
    exit()
if len(set(flights['tailnum'].unique()) - set(planes['tailnum'])) > 0 and len(set(set(flights['tailnum'].unique()) - set(planes['tailnum'])) - {"NULL"}) > 0:
    print(set(flights['tailnum'].unique()) - set(planes['tailnum']))
    print("data is not clean yet... Error on: len(set(flights['tailnum'].unique()) - set(planes['tailnum']))")
    exit()
if len(set(flights['carrier']) - set(airlines['carrier'])):
    print("data is not clean yet... Error on: len(set(flights['carrier']) - set(airlines['carrier']))")
    exit()


print("The data is clean :) ")

planes.to_csv(r'database/clean_csv/clean_planes.csv', index = False)
airports.to_csv(r'database/clean_csv/clean_airports.csv', index = False)
airlines.to_csv(r'database/clean_csv/clean_airlines.csv', index = False)
weather.to_csv(r'database/clean_csv/clean_weather.csv', index = False)
flights.to_csv(r'database/clean_csv/clean_flights.csv', index = False)






