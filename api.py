from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, marshal_with, fields
import asyncio


app = Flask(__name__)
api = Api(app)


# format to be serialized for relevant fields
video_fields = {
    'id': fields.Integer,
    'url': fields.String,
}
video_info = {
    'id': fields.Integer,
    'title': fields.String,
    'description': fields.String,
    'thumbnail': fields.String,
    'views': fields.Integer,
    'duration': fields.String,
    'like_count': fields.Integer,
}

        








if __name__ == '__main__':
    app.run(debug=True)

