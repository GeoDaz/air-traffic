# imports
from flask import Flask, request, jsonify, escape
from database.query import sql_query
from flask_sqlalchemy import SQLAlchemy
from database.manage_data import clean_and_insert_data
import os
from env import LOCAL_DATABASE

# const
POST = 'POST'
GET = 'GET'

# app
app = Flask(__name__)
app.secret_key = "INGR-airports-µ467913"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = LOCAL_DATABASE

db = SQLAlchemy(app)

# routes
# # airports
@app.route('/api/airports')
def airports():
    return jsonify({'airports': sql_query('SELECT * FROM airports')})


@app.route('/api/airports/<faa>')
def airport(faa):
    return jsonify({
        'airports': sql_query(
            'SELECT * FROM airports WHERE faa = %s',
            (escape(faa))
        )
    })


@app.route('/api/airports/counts')
def count_airports():
    return jsonify({
        'count_airports': sql_query('SELECT COUNT(DISTINCT faa) FROM airports')
    })


# # airlines
@app.route('/api/airlines')
def airlines():
    return jsonify({'airlines': sql_query('SELECT * FROM airlines')})


@app.route('/api/airlines/<carrier>')
def airline(carrier):
    return jsonify({
        'airlines': sql_query(
            'SELECT * FROM airlines WHERE carrier = %s',
            (escape(carrier))
        )
    })


@app.route('/api/airlines/counts')
def count_airlines():
    return jsonify({
        'count_airlines': sql_query(
            'SELECT COUNT(DISTINCT carrier) FROM airlines'
        )
    })


# # flights
@app.route('/api/flights')
def flights():
    return jsonify({'flights': sql_query('SELECT * FROM flights')})


@app.route('/api/flights/<int:id>')
def flight(id: int):
    return jsonify({
        'flights': sql_query(
            'SELECT * FROM flights WHERE id = %s',
            (escape(id))
        )
    })


@app.route('/api/flights/counts')
def count_flights():
    return jsonify({
        'count_flights': sql_query('SELECT COUNT(DISTINCT id) FROM flights')
    })


# run debug
if __name__ == "__main__":
    app.run(debug=True)

