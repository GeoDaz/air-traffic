# imports
from flask import Flask, request, jsonify, escape
from flask_sqlalchemy import SQLAlchemy
import os
from database.env import LOCAL_DATABASE
import json
from Routes.airports import Airports
from Routes.airlines import Airlines
from Routes.origin_airports import OriginAirports

# from Routes.airlines import get_number_destination_per_airlines
# from Routes.airports import get_airports_count, get_airports_unique_timezone, get_airports_unique_timezone_by_destination
# from Routes.flights import get_flights_count, get_most_visited_destination, get_planes_with_most_flights
# from Routes.planes import get_planes_count
from Routes.answers import Answers

from flask_restful import Api
from flask_cors import CORS, cross_origin

# const
POST = 'POST'
GET = 'GET'

# app
app = Flask(__name__)
api = Api(app)
CORS(app)

app.secret_key = "INGR-airports-µ467913"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = LOCAL_DATABASE

db = SQLAlchemy(app)

# airport routes
api.add_resource(OriginAirports, "/api/airports/origin")
api.add_resource(Airports, "/api/airports/<string:faa>")

api.add_resource(Answers, "/api/answers")
api.add_resource(Airlines, "/api/airlines/destination/count")

# run debug
if __name__ == "__main__":
    app.run(debug=True)
