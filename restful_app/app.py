# imports
from flask import Flask, request, jsonify, escape
from flask_sqlalchemy import SQLAlchemy
import os
from env import LOCAL_DATABASE
import json

from Models.db_models import Airport
from Routes.airlines import get_airlines_count
from Routes.airports import get_airports_count, get_airports_unique_timezone, get_airports_unique_timezone_by_destination, get_better_airports_by_faa
from Routes.flights import get_flights_count
from Routes.planes import get_planes_count

from flask_restful import Api

# const
POST = 'POST'
GET = 'GET'

# app
app = Flask(__name__)
api = Api(app)

app.secret_key = "INGR-airports-µ467913"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = LOCAL_DATABASE

db = SQLAlchemy(app)



# # airlines
# @app.route('/api/airlines')
# def airlines():
#     airlines = Airline.query.all()
#     return Airline.json_list(airlines)


# @app.route('/api/airlines/<carrier>')
# def airline(carrier):
#     airlines = Airline.query.filter_by(carrier=carrier)
#     return Airline.json_list(airlines)



# # airline count
# @app.route('/api/airlines/count')
# def count_airlines():
#     airlines = Airline.query.all()
#     airlines_count = len(airlines)
#     return jsonify(airlines_count)


# # flights
# @app.route('/api/flights')
# def flights():
#     flights = Flight.query.all()
#     return Flight.json_list(flights)


# @app.route('/api/flights/<int:id>')
# def flight(id: int):
#     flight = Flight.query.filter_by(id=id)
#     return Flight.json_list(flight)


# @app.route('/api/flights/count')
# def count_flights():
#     flights = Flight.query.all()
#     flights_count = len(flights)
#     return jsonify(flights_count)

# airport routes
# api.add_resource(get_all_airports, '/api/airports')
# api.add_resource(get_airports_by_faa, '/api/airports/<string:faa>')
api.add_resource(get_airports_count, '/api/airports/count')
api.add_resource(get_airports_unique_timezone, '/api/airports/timezone/count')
api.add_resource(get_airports_unique_timezone_by_destination, '/api/airports/timezone/<string:dst>')
api.add_resource(get_better_airports_by_faa, "/api/hello")

# airline routes
api.add_resource(get_airlines_count, '/api/airlines/count')

# flights routes
api.add_resource(get_flights_count, '/api/flights/count')

# planes routes
api.add_resource(get_planes_count, '/api/planes/count')


# run debug
if __name__ == "__main__":
    app.run(debug=True)

