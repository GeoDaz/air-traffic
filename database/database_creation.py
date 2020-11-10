import pymysql
import OperationalError

db_connection = pymysql.connect(
    host="db4free.net",
  	user="ingrdb",
  	passwd="db4freeIngr"
    database="airtrafficdb"
)

# prepare a cursor object using cursor() method
cursor = db.cursor()

# executing cursor with execute method and pass SQL query
#db_cursor.execute("CREATE DATABASE database")

# Open and read the file 
fd = open('airtraffic_Database.sql', 'r')
sqlFile = fd.read()
fd.close()

# all SQL commands (split on ';')
sqlCommands = sqlFile.split(';')

# Execute every command from the input file
for command in sqlCommands:
    # This will skip and report errors
    # For example, if the tables do not yet exist, this will skip over
    # the DROP TABLE commands
    try:
        cursor.execute(command)
    except OperationalError, msg:
        print "Command skipped: ", msg