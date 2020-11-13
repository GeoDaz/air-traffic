from flask_restful import Resource
from Models.db_models import Plane
from database.query import sql_query


def get_planes_count():
    count_planes = sql_query("SELECT COUNT(tailnum) FROM plane;")[0][0]
    return count_planes

def get_number_unique_planes_to_SEA():
    count_planes = sql_query(
        "SELECT COUNT(DISTINCT tailnum) FROM flight WHERE dest = 'SEA';")[0][0]
    return count_planes


def get_planes_with_most_flights(order="DESC", limit=10):
    if order != "DESC" and order != "ASC":
        return {"error": "param order must be DESC or ASC"}

    top_ten_plane = [cols[0] for cols in sql_query(
        f"SELECT tailnum, count(tailnum) AS c FROM flight WHERE tailnum IS NOT NULL GROUP BY tailnum ORDER BY c {order} limit {limit}"
    )]
    return top_ten_plane

