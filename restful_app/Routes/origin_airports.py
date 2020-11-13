from flask_restful import Resource
from flask import jsonify, send_file
from database.query import sql_query


class OriginAirports(Resource):
    def get(self):
        return jsonify({
            'airports': [{'faa': cols[0], 'name': cols[1]} for cols in sql_query(
                "SELECT flight.origin, airport.name FROM flight INNER JOIN airport ON flight.origin = airport.faa GROUP BY origin;"
            )]
        })
