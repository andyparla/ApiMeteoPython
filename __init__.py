from flask import Flask
from flask_restful import Api
from controller.MeteoController import HelloWorld

app = Flask(__name__)
api = Api(app)

api.add_resource(HelloWorld, '/api/<nombre>')


if __name__ == '__main__':
    app.run(debug=True, port=4000)
