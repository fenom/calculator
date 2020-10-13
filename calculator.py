from flask import Flask, request
from flask_restx import Resource, Api

app = Flask(__name__)
api = Api(app)

@api.route('/addition/<int:x>/<int:y>')
class Addition(Resource):
    def get(self, x, y):
        return {'sum': x + y}

@api.route('/subtraction/<int:x>/<int:y>')
class Subtraction(Resource):
    def get(self, x, y):
        return {'difference': x - y}

@api.route('/multiplication/<int:x>/<int:y>')
class Multiplication(Resource):
    def get(self, x, y):
        return {'product': x * y}

@api.route('/division/<int:x>/<int:y>')
class Division(Resource):
    def get(self, x, y):
        return {'quotient': x // y}

if __name__ == '__main__':
    app.run(debug=True)
