from flask_restful import Resource
from Models.db_models import Plane

class get_planes_count(Resource):
    def get(self):
        count_planes = sql_query("SELECT COUNT(tailnum) FROM plane;")[0][0]
        return jsonify(planes)







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