from . import *


class HelloWorld(Resource):
    def get(self, nombre: str):
        return {"Hola": nombre}
    def post(self, nombre: str, id: int):
        return {'status': 'success'}
