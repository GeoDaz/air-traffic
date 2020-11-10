import psycopg2
import urllib.parse as urlparse
import os

import pymysql

# database config
HOST = "your_host"
USERNAME = "database_username"
PASSWORD = "database_password"
DATABASE = "database_name"


# Open database connection
db = pymysql.connect(HOST, USERNAME, PASSWORD, DATABASE)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# prepare sql statement 
sql_query = "Select * from airlines where name = '%s'" % ("robert")

try:
    # execute sql query
    cursor.execute(sql_query)

    # fetch all rows in a list of lists
    result = cursor.fetchall()

    for row in result:
        print("carrier ", row[0])
        print("name ", row[0])
except:
    print("Error: unable to fetch data")

# execute SQL query using execute() method.
# cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
# data = cursor.fetchone()
# print ("Database version : %s " % data)

# disconnect from server
db.close()

