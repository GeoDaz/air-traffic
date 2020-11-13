from flask_restful import Resource
from flask import jsonify, send_file
from Utils.airlines import get_airlines_count, get_number_airline_to_SEA
from Utils.airports import get_airports_count, get_airports_unique_timezone, get_airports_with_unchangeable_timezone, get_most_used_airport_for_departure
from Utils.planes import get_planes_count, get_planes_with_most_flights, get_number_unique_planes_to_SEA
from Utils.flights import get_most_visited_destination, get_flight_to_houston, get_number_flights_NYC_SEA, get_number_unique_flights_by_destination


class Answers(Resource):
    def get(self):
        answers = dict()
        # QUESTION 2 - Combien y-a-t-il d’aéroports, de compagnies, de destinations, d’avions et de fuseaux horaires ?
        answers["question_2"] = [get_airlines_count(), get_airports_count(), get_airports_unique_timezone(), get_planes_count()]

        # QUESTION 3 - Combien y-a-t-il de zones aux Etats-Unis où on ne passe pas à l’heure d’été (indice : colonne dst) ?
        answers["question_3"] = get_airports_with_unchangeable_timezone()

        # QUESTION 4 - Quel est l’aéroport de départ le plus emprunté ? Quelles sont les 10 destinations les plus (moins) prisées ? Quelle sont les 10 avions qui ont le plus (moins) décollé ?
        answers["question_4"] = [get_most_used_airport_for_departure(), get_most_visited_destination(), get_most_visited_destination(order="DESC"), get_planes_with_most_flights(), get_planes_with_most_flights(order="ASC")]

        # QUESTION 5 - Trouver combien chaque compagnie a desservi de destination ; combien chaque compagnie a desservie de destination par aéroport d’origine. Réaliser les graphiques adéquats qui synthétisent ces informations ?
        # image

        # QUESTION 6 - Trouver tous les vols ayant atterri à Houston (IAH ou HOU) (indice : 9313 vols). Combien de vols partent de NYC airports vers Seattle (indice : 3923 vols), combien de compagnies desservent cette destination (indice : 5 compagnies) et combien d’avions “uniques” (indice : 935 avions) ?
        answers["question_6"] = [get_flight_to_houston(), get_number_airline_to_SEA(), get_number_flights_NYC_SEA(), get_number_unique_planes_to_SEA()]

        # QUESTION 7 - Trouver le nombre de vols unique par destination voir l’aperçu. Trier les vols suivant la destination, l’aéroport d’origine, la compagnie dans un ordre alphabétique croissant (en réalisant les jointures nécessaires pour obtenir les noms des explicites des aéroports) ? indice : voir l’aperçu
        answers["question_7"] = get_number_unique_flights_by_destination()

        return jsonify(answers)
