from flask_restful import Resource
from flask import jsonify, send_file
from Utils.airports import get_airport_info

class Airport(Resource):
    def get(self):
        airport_info = dict()
        needed_airports = ["EWR", "JFK", "LGA"]
        test = get_airport_info("EWR")
        for airport in needed_airports:
            airport[airport] = get_airport_info(airport)

        return jsonify(test)

