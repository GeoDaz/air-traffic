from app import db
from manage_data import clean_and_insert_data
import os 

db.create_all()
clean_and_insert_data()