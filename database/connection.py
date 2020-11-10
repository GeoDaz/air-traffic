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




# try:
#     # url = urlparse.urlparse(
#     #     "postgres://ebhgdxmbrnykla:4fdc3642f0e03c7782d38ac08116d66cd29381a224076807eac5e0431fc347c8@ec2-54-75-199-252.eu-west-1.compute.amazonaws.com:5432/d2576apdblvm7i")

#     # dbname = url.path[1:]
#     # user = url.username
#     # password = url.password
#     # host = url.hostname
#     # port = url.port

#     connection = psycopg2.connect(
#         dbname="airtrafficdb",
#         user="ingrdb",
#         password="db4freeIngr",
#         host="db4free",
#         port=3306
#     )
#     cursor = connection.cursor()
#     print(connection)

#     postgres_insert_query = """ INSERT INTO airlines (carrier, name) VALUES (%s,%s)"""
#     record_to_insert = ('{I5}', '{Ines inc}')
#     cursor.execute(postgres_insert_query, record_to_insert)

#     connection.commit()
#     count = cursor.rowcount
#     print(count, "Record inserted successfully into mobile table")

# except (Exception, psycopg2.Error) as error:
#     if(connection):
#         print("Failed to insert record into mobile table", error)

# finally:
#     # closing database connection.
#     if(connection):
#         cursor.close()
#         connection.close()
#         print("PostgreSQL connection is closed")
