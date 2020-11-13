from flask_restful import Resource
from flask import jsonify, send_file
from Utils.airports import get_airport_info
from flask_restful import Resource
from flask import jsonify, send_file
from database.query import sql_query
import matplotlib.pyplot as plt
import pandas
import io


class Airlines(Resource):
    def get(self):
        plt.rcParams['figure.figsize'] = (10, 10)

        count_dest = sql_query("""SELECT airline.name, COUNT(flight.dest) FROM flight 
            INNER JOIN airline ON flight.carrier = airline.carrier 
            GROUP BY flight.carrier LIMIT 0, 25;""")

        airlines_dests = pandas.DataFrame(
            count_dest, columns=['Compagnie', 'Nombre de destination']
        )
        bytes_obj = io.BytesIO()

        try:
            plt.bar(
                x=airlines_dests["Compagnie"],
                height=airlines_dests["Nombre de destination"],
                data=airlines_dests
            )
            plt.xticks(rotation='vertical')
            plt.savefig(bytes_obj, format="png")
            bytes_obj.seek(0)
        except expression as identifier:
            print("Error saving the image")
        finally:
            plt.close()

        return send_file(
            bytes_obj,
            attachment_filename='plot.png',
            mimetype='image/png'
        )
