from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from controller.MeteoController import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/api/<nombre>')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
