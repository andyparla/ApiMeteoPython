from flask import Flask
from flask_restful import Api, Resource, reqparse


class HelloWorld(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()

    def get(self, nombre: str):
        return {"Hola": nombre}

    def get(self, nombre: str):
        self.parser.add_argument('dni', type=str, required=True, location='form', help="DNI VACIO no ENVIADO")
        dni = self.parser.parse_args()
        if dni.get("dni") == "":
            return f"DNI de {nombre} ES VACIOOOOO"
        else:
            return {f"DNI de {nombre}": dni.get("dni")}

    def post(self, nombre: str, id: int):
        return {'status': 'success'}


""" TIPOS DE ARGUMENTOS
ESTE ADD COMPRUEBA QUE EL ARGUMENTO FOO VIENE ONE O TWO EN OTRO CASO DEVUELVE ERROR
parser.add_argument('foo', choices=('one', 'two'), help='Bad choice: {error_msg}')

# Look only in the POST body
parser.add_argument('name', type=int, location='form')
# Look only in the JSON body
parser.add_argument('name', type=int, location='json')
# Look only in the querystring
parser.add_argument('PageSize', type=int, location='args')
# From the request headers
parser.add_argument('User-Agent', location='headers')
# From http cookies
parser.add_argument('session_id', location='cookies')
# From file uploads
parser.add_argument('picture', type=werkzeug.datastructures.FileStorage, location='files')
"""

