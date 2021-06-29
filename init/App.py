from flask import Flask, jsonify, request
from flask_restful import Api, Resource
#from ApiTest.controller.Controller import EstacionMeteo
from ..controller.Controller import meteo

app = Flask(__name__)
api = Api(app)
app.register_blueprint(meteo)


api.add_resource(EstacionMeteo, '/api/<nombre>')

if __name__ == '__main__':
    app.run(debug=True, port=4000)