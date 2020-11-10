import pymysql


def sql_query(query :str):
    # Open database connection
    db = pymysql.connect(host='db4free.net', user='ingrdb', password='db4freeIngr', db='airtrafficdb')

    # prepare a cursor object using cursor() method
    cursor = db.cursor()

    try:
        # execute sql query
        cursor.execute(query)

        # fetch all rows in a list of lists
        result = cursor.fetchall()

    except Exception as e:
        raise e

    finally:
        # disconnect from server
        db.close()
    
    return result

print(sql_query("INSERT INTO airlines (carrier, name) VALUES ('truc', 'test')"))