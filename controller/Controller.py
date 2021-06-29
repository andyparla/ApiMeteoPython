from flask_restful import Resource
from flask import Blueprint

#Blueprints: https://www.youtube.com/watch?v=3Yz6QanCSaA
meteo = Blueprint('meteo', __name__)


class EstacionMeteo(Resource):
    def get(self, nombre: str):
        return {"Hola": nombre}
    def post(self, nombre: str, id: int):
        return {'status': 'success'}
