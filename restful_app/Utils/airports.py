from flask_restful import Resource
from Models.db_models import Airport
from flask import jsonify
from database.query import sql_query


class get_airports_by_faa(Resource):
    def get_airports_by_faa(self, faa):
        airports = Airport.query.filter_by(faa=faa)  # Airport.faa.in_(fil)
        return Airport.json_list(airports)


def get_airports_count():
    airports_count = sql_query("select COUNT(faa) from airport")[0][0]
    return airports_count


def get_airports_unique_timezone():
    count_tz = sql_query("SELECT COUNT(DISTINCT tz) FROM airport;")[0][0]
    return count_tz


def get_airports_with_unchangeable_timezone():
    count_zones = sql_query(
        "SELECT count(DISTINCT tzone) FROM airport WHERE dst = 'N';")[0][0]
    return count_zones


def get_most_used_airport_for_departure():
    better_airport_faa = sql_query(
        """SELECT ap.name FROM airport AS ap 
        INNER JOIN (
            SELECT origin FROM flight GROUP BY origin ORDER BY COUNT(id) DESC LIMIT 1
        ) as s2 on ap.faa = s2.origin LIMIT 0, 25""")[0][0]

    return better_airport_faa


def get_airport_info(faa):
    airport_info = sql_query(
        "SELECT f.flight, ap1.name, ap2.name, al.name, f.tailnum, f.time_hour FROM airport AS ap1 " +
        "INNER JOIN flight AS f on ap1.faa = f.origin " +
        "INNER JOIN airport AS ap2 on ap2.faa = f.dest " +
        "INNER JOIN airline AS al on al.carrier = f.carrier " +
        "WHERE ap1.faa = %s ORDER BY f.time_hour LIMIT 0, 25;",
        (faa)
    )
    return airport_info

# tzone, dep_time, shced_dep_time, dep_delay, arr_time, sched_arr_time, arr_delay, carrier, flight, tailnum, origin, dest, air_time, distance, time_hour

    # top_ten_dest = [cols[0] for cols in sqlquery(
    #     'SELECT ap.name FROM airport AS ap WHERE ap.faa IN ('
    #         + ','.join(['%s' for  in top_ten_dest_faa])
    #         + ');',
    #     top_ten_dest_faa
    # )]
    # return ', '.join(top_ten_dest)


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
