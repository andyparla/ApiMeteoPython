from flask_restful import Resource, reqparse
from flask import Blueprint, request
from dtos.MeteoBean import MeteoBean
from service.Service import MeteoService
import logging

# Blueprints: https://www.youtube.com/watch?v=3Yz6QanCSaA
meteo = Blueprint('meteo', __name__)


class EstacionMeteoController(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self, chipId: str):
        logging.info(f"Se ha recibido el id {chipId}")
        lstMeteo = MeteoService().obtenerInfoById(chipId)
        return {"Hola": chipId}

    def delete(self, chipId: str):
        return {'status': 'success'}


class EstacionMeteoControllerPost(Resource):

    def post(self):
        chipData = request.get_json()
        meteoBean = MeteoBean(chipData['chipData']['chipId'],
                              chipData['chipData']['temperatura'],
                              chipData['chipData']['humedad'],
                              chipData['chipData']['hic'],
                              chipData['chipData']['fechaGrabado'])

        print(MeteoService().obtenerInfoById(meteoBean.get_chip_id()))
        return {'status': 'success'}
