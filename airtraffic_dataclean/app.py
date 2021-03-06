from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from env import DATABASE

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE

db = SQLAlchemy(app)


class Airline(db.Model):
    carrier = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))


class Airport(db.Model):
    faa = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    alt = db.Column(db.Integer)
    tz = db.Column(db.Integer)
    dst = db.Column(db.String(100))
    tzone = db.Column(db.String(100))


class Plane(db.Model):
   tailnum = db.Column(db.String(100), primary_key=True)
   year = db.Column(db.Integer)
   type = db.Column(db.String(100))
   manufacturer = db.Column(db.String(100))
   model = db.Column(db.String(100))
   engines = db.Column(db.String(100))
   seats = db.Column(db.Integer)
   speed = db.Column(db.Integer)
   engine = db.Column(db.String(100))


class Weather(db.Model):
    origin = db.Column(db.String(100), db.ForeignKey(
        "airport.faa"), primary_key=True)
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


class Flight(db.Model):
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
    carrier = db.Column(db.String(100), db.ForeignKey(
        'airline.carrier'), nullable=True)
    flight = db.Column(db.String(100))
    tailnum = db.Column(db.String(100), db.ForeignKey(
        'plane.tailnum'), nullable=True)
    origin = db.Column(db.String(100), db.ForeignKey(
        'airport.faa'), nullable=True)
    dest = db.Column(db.String(100), db.ForeignKey(
        'airport.faa'), nullable=True)
    air_time = db.Column(db.Integer)
    distance = db.Column(db.Integer)
    hour = db.Column(db.Integer)
    minute = db.Column(db.Integer)
    time_hour = db.Column(db.DateTime)
    flight_origin = db.relationship("Airport", foreign_keys=[origin])
    flight_dest = db.relationship("Airport", foreign_keys=[dest])

    
# run debug
if __name__ == "__main__":
    app.run(debug=True)
