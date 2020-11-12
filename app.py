# imports
from flask import Flask, request, jsonify, escape
from flask_sqlalchemy import SQLAlchemy
from database.manage_data import clean_and_insert_data
import os
from env import LOCAL_DATABASE
import json
from flask_serialize import FlaskSerializeMixin

# const
POST = 'POST'
GET = 'GET'

# app
app = Flask(__name__)
app.secret_key = "INGR-airports-µ467913"

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = LOCAL_DATABASE

db = SQLAlchemy(app)

class Airline(db.Model, FlaskSerializeMixin):
    carrier = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    # flights = db.relationship("Flight", backref='airline')


class Airport(db.Model, FlaskSerializeMixin):
    faa = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    alt = db.Column(db.Integer)
    tz = db.Column(db.Integer)
    dst = db.Column(db.String(100))
    tzone = db.Column(db.String(100))
    # flights = db.relationship("Flight", backref='airport', lazy=True)


class Plane(db.Model, FlaskSerializeMixin):
   tailnum = db.Column(db.String(100), primary_key=True)
   year = db.Column(db.Integer)
   type = db.Column(db.String(100))
   manufacturer = db.Column(db.String(100))
   model = db.Column(db.String(100))
   engines = db.Column(db.String(100))
   seats = db.Column(db.Integer)
   speed = db.Column(db.Integer)
   engine = db.Column(db.String(100))
#    flights = db.relationship("Flight", backref='plane', lazy=True)


class Weather(db.Model, FlaskSerializeMixin):
    origin = db.Column(db.String(100), db.ForeignKey("airport.faa"), primary_key=True)
    year = db.Column(db.Integer, primary_key=True)
    month = db.Column(db.Integer, primary_key=True)
    day = db.Column(db.Integer, primary_key=True)
    hour = db.Column(db.Integer, primary_key=True)
    temp = db.Column(db.Float)
    dewp = db.Column(db.Float)
    humid = db.Column(db.Float)
    wind_dir = db.Column(db.Integer)
    wind_speed = db.Column(db.Float)
    wind_gust = db.Column(db.Float)
    precip = db.Column(db.Integer)
    pressure = db.Column(db.Float)
    visib = db.Column(db.Integer)
    time_hour = db.Column(db.DateTime)
    # airport = db.relationship("Airport", backref='weather', lazy=True)


class Flight(db.Model, FlaskSerializeMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    year = db.Column(db.Integer)
    month = db.Column(db.Integer)
    day = db.Column(db.Integer)
    dep_time = db.Column(db.Integer)
    sched_dep_time = db.Column(db.Integer)
    dep_delay = db.Column(db.Integer)
    arr_time = db.Column(db.Integer)
    sched_arr_time = db.Column(db.Integer)
    arr_delay = db.Column(db.Integer)
    carrier = db.Column(db.String(100), db.ForeignKey('airline.carrier'), nullable=True)
    flight = db.Column(db.String(100))
    tailnum = db.Column(db.String(100), db.ForeignKey('plane.tailnum'), nullable=True)
    origin = db.Column(db.String(100), db.ForeignKey('airport.faa'), nullable=True)
    dest = db.Column(db.String(100), db.ForeignKey('airport.faa'), nullable=True)
    air_time = db.Column(db.Integer)
    distance = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    minute = db.Column(db.Integer)
    time_hour = db.Column(db.DateTime)
    flight_origin = db.relationship("Airport", foreign_keys=[origin])
    flight_dest = db.relationship("Airport", foreign_keys=[dest])


# routes
# # airports
@app.route('/api/airports')
def airports():
    airports = Airport.query.all()
    return Airport.json_list(airports)


@app.route('/api/airports/<faa>')
def airport(faa):
    fil = ["04G", "06A"]
    airports = Airport.query.filter(Airport.faa.in_(fil))
    return Airport.json_list(airports)


@app.route('/api/airports/counts')
def count_airports():
    airlines = Airline.query.all()
    airlines_count = len(airlines)
    return jsonify(airlines_count)


# airlines
@app.route('/api/airlines')
def airlines():
    airlines = Airline.query.all()
    return Airline.json_list(airlines)


@app.route('/api/airlines/<carrier>')
def airline(carrier):
    airlines = Airline.query.filter_by(carrier=carrier)
    return Airline.json_list(airlines)


@app.route('/api/airlines/counts')
def count_airlines():
    airlines = Airline.query.all()
    airlines_count = len(airlines)
    return jsonify(airlines_count)


# flights
@app.route('/api/flights')
def flights():
    flights = Flight.query.all()
    return Flight.json_list(flights)


@app.route('/api/flights/<int:id>')
def flight(id: int):
    flight = Flight.query.filter_by(id=id)
    return Flight.json_list(flight)


@app.route('/api/flights/counts')
def count_flights():
    flights = Flight.query.all()
    flights_count = len(flights)
    return jsonify(flights_count)


# run debug
if __name__ == "__main__":
    app.run(debug=True)

