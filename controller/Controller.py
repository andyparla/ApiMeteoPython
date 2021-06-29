import flask

#Blueprints: https://www.youtube.com/watch?v=3Yz6QanCSaA
meteo = flask.Blueprint('meteo', __name__)

class EstacionMeteo(Resource):
    def get(self, nombre: str):
        return {"Hola": nombre}
    def get(self, nombre: str, apellidos: str):
        return {f"Hola {nombre} {apellidos}"}
    def post(self, nombre: str, id: int):
        return {'status': 'success'}

api.add_resource(EstacionMeteo, '/api/<nombre>')
