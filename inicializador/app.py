from controller.MeteoController import HelloWorld, Flask, Api, Resource

app = Flask(__name__)
api = Api(app)
api.add_resource(HelloWorld, '/api/<nombre>')

if __name__ == '__main__':
    app.run(debug=True, port=4000)


