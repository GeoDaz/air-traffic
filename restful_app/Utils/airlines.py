from flask_restful import Resource
from flask import jsonify, send_file
from database.query import sql_query
import matplotlib.pyplot as plt
import pandas
import io


def get_airlines_count():
    count_airlines = sql_query("SELECT COUNT(carrier) FROM airline;")[0][0]
    return count_airlines


# 6.3) Combien de compagnies desservent cette destination (indice : 5 compagnies) ?
def get_number_airline_to_SEA():
    count_airlines = sql_query(
        "SELECT COUNT(DISTINCT carrier) FROM flight WHERE dest = 'SEA';")[0][0]
    return count_airlines


# class img_test(Resource):
#     def get():
#         bytes_obj = do_plot()
#         return send_file(bytes_obj, attachment_filename='../assets/test_img.png', mimetype='image/png')
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
