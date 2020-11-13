from flask_restful import Resource
from flask import jsonify, send_file
from Utils.airports import get_airport_info


class Airports(Resource):
    def get(self, faa):
        return jsonify({'flights': [
            {
                'flight': flight[0],
                'origin': flight[1],
                'dest': flight[2],
                'airline': flight[3],
                'plane': flight[4],
                'date': flight[5],
            } for flight in get_airport_info(faa)
        ]})
