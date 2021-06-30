from flask import Flask
from flask_restful import Api
import os
from controller.Controller import meteo
from controller.Controller import EstacionMeteoController, EstacionMeteoControllerPost
from dao.ConexionMariaDB import ConexionMariaDB

app = Flask(__name__)
app.secret_key = os.urandom(64)

api = Api(app)

app.register_blueprint(meteo)

api.add_resource(EstacionMeteoController, '/data/<chipId>')
api.add_resource(EstacionMeteoControllerPost, '/data')


@app.before_first_request
def beforefreq():
    ConexionMariaDB().getInstancia()

if __name__ == '__main__':
    app.run(debug=True, port=4000)