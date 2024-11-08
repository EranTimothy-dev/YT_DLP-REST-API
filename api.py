from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields


app = Flask(__name__)
api = Api(app)


video_fields = {
    'id': fields.Integer,
    'url': fields.String,
}

        



if __name__ == '__main__':
    app.run(debug=True)

