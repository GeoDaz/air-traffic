from flask_restful import Resource
from Models.db_models import Airline
from flask import jsonify
from database.query import sql_query

class get_airlines_count(Resource):
    def get(self):
        count_airlines = sql_query("SELECT COUNT(carrier) FROM airline;")[0][0]
        return jsonify(count_airlines)


class get_number_destination_per_airlines(Resource):
    def get(self):
        count_dest = sql_query("""SELECT airline.name, COUNT(flight.dest) FROM flight 
                                INNER JOIN airline ON flight.carrier = airline.carrier 
                                GROUP BY flight.carrier;""")
        return jsonify(count_dest)


# 6.3) Combien de compagnies desservent cette destination (indice : 5 compagnies) ?
class get_number_airline_to_SEA():
    count_airlines = sql_query("SELECT COUNT(DISTINCT carrier) FROM flight WHERE dest = 'SEA';")[0][0]
    return jsonify(count_airlines)


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
#     return jsonify(airlines_count)