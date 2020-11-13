from flask_restful import Resource
from Models.db_models import Plane
from database.query import sql_query

def get_planes_count():
    count_planes = sql_query("SELECT COUNT(tailnum) FROM plane;")[0][0]
    return count_planes

    
# 6.4) Combien d’avions “uniques” (indice : 935 avions) ?
def get_number_unique_planes_to_SEA():
    count_planes = sql_query("SELECT COUNT(DISTINCT tailnum) FROM flight WHERE dest = 'SEA';")[0][0]
    return count_planes


def get_planes_with_most_flights(order="DESC", limit=10):
    if order != "DESC" and order != "ASC": return {"error": "param order must be DESC or ASC"}

    top_ten_plane = [cols[0] for cols in sql_query(
        f"select tailnum, count(tailnum) as c from flight where tailnum is not null GROUP BY tailnum order by c {order} limit {limit}"
    )]
    return top_ten_plane


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