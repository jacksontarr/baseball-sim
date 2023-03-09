from flask import Flask
from flask_restful import Resource, Api
from api.management import *
from db.utils import rebuild_tables

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('id', type=int)

api.add_resource(Init, '/manage/init')
api.add_resource(Version, '/manage/version')

if __name__ == '__main__':
    rebuild_tables()
    app.run(debug=True)