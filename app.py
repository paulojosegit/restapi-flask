
from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)


class Users(Resource):
    def get(self):
        return {'message': 'users'}


class User(Resource):
    def get(self):
        return {'message': 'cpf'}


api.add_resource(Users, '/users')
api.add_resource(User, '/user/')

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
