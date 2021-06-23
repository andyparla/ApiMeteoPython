from flask import Flask, jsonify, request
from flask_restful import Resource


class HelloWorld(Resource):
    def get(self, nombre: str):
        return {"Hola": nombre}
    def post(self, nombre: str, id: int):
        return {'status': 'success'}
