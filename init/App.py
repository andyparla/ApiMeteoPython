import Flask, Api, EstacionMeteo

app = Flask(__name__)
api = Api(app)


api.add_resource(EstacionMeteo, '/api/<nombre>')

if __name__ == '__main__':
    app.run(debug=True, port=4000)