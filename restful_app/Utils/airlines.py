from flask_restful import Resource
from flask import jsonify, send_file
from database.query import sql_query
import matplotlib.pyplot as plt
import pandas
import io


def get_airlines_count():
    count_airlines = sql_query("SELECT COUNT(carrier) FROM airline;")[0][0]
    return count_airlines


class get_number_destination_per_airlines(Resource):
    def get(self):
        count_dest = sql_query("""SELECT airline.name, COUNT(flight.dest) FROM flight 
                                INNER JOIN airline ON flight.carrier = airline.carrier 
                                GROUP BY flight.carrier;""")
        
        airlines_dests = pandas.DataFrame(count_dest, columns=['Compagnie', 'Nombre de destination'])
        bytes_obj = io.BytesIO()
        try:
            plt.bar(x=airlines_dests["Compagnie"], height=airlines_dests["Nombre de destination"], data=airlines_dests)
            plt.savefig(bytes_obj, format="png")
            bytes_obj.seek(0)
        except expression as identifier:
            print("Error saving the image")
        finally:
            plt.close()
        
        return send_file(bytes_obj,
                        attachment_filename='plot.png',
                         mimetype='image/png')


# 6.3) Combien de compagnies desservent cette destination (indice : 5 compagnies) ?
def get_number_airline_to_SEA():
    count_airlines = sql_query(
        "SELECT COUNT(DISTINCT carrier) FROM flight WHERE dest = 'SEA';")[0][0]
    return count_airlines


# class img_test(Resource):
#     def get():
#         bytes_obj = do_plot()
#         return send_file(bytes_obj, attachment_filename='../assets/test_img.png', mimetype='image/png')
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
