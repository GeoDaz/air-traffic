from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from database.manage_data import clean_and_insert_data
import os
from env import LOCAL_DATABASE

app = Flask(__name__)

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = LOCAL_DATABASE

db = SQLAlchemy(app)


@app.route('/')
def index():
    return "hello world"


if __name__ == "__main__":
    app.run(debug=True)