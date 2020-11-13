from flask_restful import Resource
from Models.db_models import Flight
from database.query import sql_query
from flask import jsonify

def get_flights_count(self):
    count_dest = sql_query("SELECT COUNT(DISTINCT dest) FROM flight;")[0][0]
    return count_dest


def get_most_visited_destination(order="ASC", limit=10):
    if order != "ASC" and order != "DESC": return {"error": "param must be ASC or DESC"}

    top_ten_dest_faa = [cols[0] for cols in sql_query(
        f"SELECT ap.name FROM airport AS ap INNER JOIN (SELECT dest FROM flight GROUP BY dest ORDER BY COUNT(id) {order} LIMIT {limit}) as f on ap.faa = f.dest"
    )]
    return top_ten_dest_faa

def get_flight_to_houston():
    flights_to_houston = sql_query("SELECT flight, origin, dest, time_hour FROM flight WHERE dest = 'IAH' OR dest = 'HOU' ORDER BY flight.flight;")
    return flights_to_houston


def get_number_flights_NYC_SEA():
    count_flights = sql_query("SELECT COUNT(flight) FROM flight WHERE (origin = 'JFK' OR origin = 'EWR' OR origin = 'LGA') AND dest = 'SEA';")[0][0]
    return count_flights


# question 7
def get_number_unique_flights_by_destination():
    count_flight_by_destination = sql_query("""SELECT airport.name, COUNT(DISTINCT flight.flight) as counter FROM flight 
                                    INNER JOIN airport ON flight.dest = airport.faa 
                                    GROUP BY flight.dest ORDER BY counter DESC""")

    return count_flight_by_destination

#         # routes
# # # airports
# @app.route('')
# def airports():
    

# @app.route('')
# def airport(faa):
#     fil = ["04G", "06A"]
#     airports = Airport.query.filter(Airport.faa.in_(fil))
#     return Airport.json_list(airports)

# # airport count
# @app.route('')
# def count_airports():
#     airlines = Airline.query.all()
#     airlines_count = len(airlines)
#     return airlines_count