import pymysql
# from os import environ
from database.env import HOST, USER, PASSWORD, DB_NAME, PORT


def sql_query(query: str, values=None):
    # Open database connection
    db = pymysql.connect(
        host=HOST,
        user=USER,
        password=PASSWORD,
        db=DB_NAME,
        port=PORT
    )

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        # execute sql query
        if(values):
            cursor.execute(query, values)
        else:
            cursor.execute(query)

        # fetch all rows in a list of lists
        result = cursor.fetchall()

    except Exception as e:
        raise e

    finally:
        # disconnect from server
        db.close()

    return result
