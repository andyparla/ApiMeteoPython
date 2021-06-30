from flask_restful import Resource, reqparse
from flask import Blueprint, request

#Blueprints: https://www.youtube.com/watch?v=3Yz6QanCSaA
meteo = Blueprint('meteo', __name__)


class EstacionMeteoController(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self, chipId: str):
        return {"Hola": chipId}
    def delete(self, chipId: str):
        return {'status': 'success'}

class EstacionMeteoControllerPost(Resource):

    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('chipData', required=True, help="No se han recibido los datos")

    def post(self):
        chipData = self.parser.parse_args(strict=True)
        print(chipData['chipData'])
        return {'status': 'success'}
