# import os
import pymysql
from env import HOST, USER, PASSWORD, DB_NAME, PORT

# print(os.path.isfile('database/airtraffic_database.sql'))

db = pymysql.connect(
    host=HOST,
    user=USER,
    password=PASSWORD,
    db=DB_NAME,
    port=PORT,
)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# Open and read the file
fd = open('database/airtraffic_database.sql', 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')

# Execute every command from the input file
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    print(command)
    try:
        cursor.execute(command)
    except Exception as msg:
        print("Command skipped :", msg)

db.close()
