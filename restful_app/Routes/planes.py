from flask_restful import Resource
from flask import jsonify, send_file
from Utils.airports import get_airport_info
from flask_restful import Resource
from flask import jsonify, send_file
from database.query import sql_query
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')  # nopep8
import pandas
import io
from Utils.planes import get_planes_with_most_flights


class Planes(Resource):
    def get(self):
        plt.rcParams['figure.figsize'] = (10, 10)

        top_ten_planes = get_planes_with_most_flights()

        planes = pandas.DataFrame(
            top_ten_planes, columns=['Avions', 'Nombre de vols']
        )

        bytes_obj = io.BytesIO()
        try:
            plt.bar(
                x=planes["Avions"],
                height=planes["Nombre de vols"],
                data=planes
            )
            plt.title("Avions par vols", loc='center', pad=None)
            plt.xticks(rotation='vertical')
            plt.savefig(bytes_obj, format="png")
            bytes_obj.seek(0)
        except EOFError as e:
            print("Error saving the image", e)
        finally:
            plt.close()

        return send_file(
            bytes_obj,
            attachment_filename='planes.png',
            mimetype='image/png'
        )
