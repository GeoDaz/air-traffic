from flask_restful import Resource
from Models.db_models import Airport
from flask import jsonify
from database.query import sql_query
      

class get_airports_by_faa(Resource):
    def get(self, faa):
        airports = Airport.query.filter_by(faa=faa) #Airport.faa.in_(fil)
        return Airport.json_list(airports)


class get_airports_count(Resource):
    def get(self):
        airports_count = sql_query("select COUNT(faa) from airport")[0][0]
        return jsonify(airports_count)


class get_airports_unique_timezone(Resource):
    def get(self):
        count_tz = sql_query("SELECT COUNT(DISTINCT tz) FROM airport;")[0][0]
        return jsonify(count_tz)


class get_airports_unique_timezone_by_destination(Resource):
    def get(self, dst):
        count_zones = sql_query("SELECT count(DISTINCT tzone) FROM airport WHERE dst = 'N';")[0][0]
        return jsonify(count_zones)


# TODO: not working, try making it in one query
class get_better_airports_by_faa(Resource):
    def get(self):
        better_airport_faa = sql_query("SELECT origin FROM flight GROUP BY origin ORDER BY COUNT(id) DESC LIMIT 1;")[0][0]

        print(better_airport_faa)

        # better_airport = sql_query('SELECT ap.name FROM airport AS ap WHERE ap.faa = %s', (better_airport_faa))[0][0]

        return jsonify(better_airport_faa)




# def get_top_dest(desc=True, limit=10):
#     top_ten_dest_faa = [cols[0] for cols in sql_query(
#         f"SELECT dest FROM flight GROUP BY dest ORDER BY COUNT(id) {'DESC' if desc else 'ASC'} LIMIT {limit};"
#     )]
#     top_ten_dest = [cols[0] for cols in sqlquery(
#         'SELECT ap.name FROM airport AS ap WHERE ap.faa IN ('
#             + ','.join(['%s' for  in top_ten_dest_faa])
#             + ');', 
#         top_ten_dest_faa
#     )]
#     return ', '.join(top_ten_dest)




# better_airport_faa = sql_query(
#     "SELECT origin FROM flight GROUP BY origin ORDER BY COUNT(id) DESC LIMIT 1;"
# )[0][0]
# better_airport = sql_query('SELECT ap.name FROM airport AS ap WHERE ap.faa = %s', (better_airport_faa))[0][0]
# print(f"L'aéroport de départ le plus emprunté est {better_airport}.")








#         # routes
# # # airports
# @app.route('')
# def airports():
    

# @app.route('')
# def airport(faa):
#     fil = ["04G", "06A"]
#     airports = Airport.query.filter(Airport.faa.in_(fil))
#     return Airport.json_list(airports)

# # airport count
# @app.route('')
# def count_airports():
#     airlines = Airline.query.all()
#     airlines_count = len(airlines)
#     return jsonify(airlines_count)