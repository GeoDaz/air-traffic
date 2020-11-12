# import pymysql
# # from os import environ
# from database.env import HOST, USER, PASSWORD, DB_NAME


# def sql_query(query: str):
#     # Open database connection
#     db = pymysql.connect(
#         # host=environ.get('HOST'),
#         # user=environ.get('USER'),
#         # password=environ.get('PASSWORD'),
#         # db=environ.get('DB_NAME')
#         host=HOST,
#         user=USER,
#         password=PASSWORD,
#         db=DB_NAME
#     )

#     # prepare a cursor object using cursor() method
#     cursor = db.cursor()

#     try:
#         # execute sql query
#         cursor.execute(query)

#         # fetch all rows in a list of lists
#         result = cursor.fetchall()

#     except Exception as e:
#         raise e

#     finally:
#         # disconnect from server
#         db.close()

#     return result


# #print(sql_query("SELECT * FROM airlines"))
