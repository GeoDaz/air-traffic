import pandas
import io
from database.query import sql_query
from Utils.airports import get_airport_info
from flask import jsonify, send_file
from flask_restful import Resource
import matplotlib
matplotlib.use('Agg')  # nopep8
import matplotlib.pyplot as plt


class Airlines(Resource):
    def get(self, use_origin=False):
        plt.rcParams['figure.figsize'] = (10, 7)
        bytes_obj = io.BytesIO()

        if use_origin:
            count_dest = sql_query(
                "SELECT airline.name, airport.name, COUNT(flight.dest) FROM flight " +
                "INNER JOIN airline ON flight.carrier = airline.carrier " +
                "INNER JOIN airport ON flight.origin = airport.faa " +
                "GROUP BY flight.carrier, flight.origin;"
            )
            airlines_dests = pandas.DataFrame(
                count_dest,
                columns=['Compagnie', 'Origine', 'Nombre de destination']
            )
            airlines_dests['Compagnie'] = airlines_dests[['Compagnie', 'Origine']].apply(
                lambda x: ' - '.join(x), axis=1
            )
        else:
            count_dest = sql_query(
                "SELECT airline.name, COUNT(flight.dest) FROM flight " +
                "INNER JOIN airline ON flight.carrier = airline.carrier " +
                "GROUP BY flight.carrier;"
            )
            airlines_dests = pandas.DataFrame(
                count_dest,
                columns=['Compagnie', 'Nombre de destination']
            )

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
