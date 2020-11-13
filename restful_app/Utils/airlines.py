from flask_restful import Resource
from flask import jsonify, send_file
from database.query import sql_query
import matplotlib.pyplot as plt
import pandas
import io


def get_airlines_count():
    count_airlines = sql_query("SELECT COUNT(carrier) FROM airline;")[0][0]
    return count_airlines


def get_number_airline_to_SEA():
    count_airlines = sql_query(
        "SELECT COUNT(DISTINCT carrier) FROM flight WHERE dest = 'SEA';")[0][0]
    return count_airlines

