from app import db
from database.manage_data import clean_and_insert_data
import os 

db.create_all()
clean_and_insert_data()


