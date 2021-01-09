
from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug

app = Flask(__name__)
api = Api(app)

class Menu(Resource):
    def get(self):

        return {'Menu': 'use /1 to VideoCoding /2 to AudioCoding'}

class VideoCoding(Resource):
    def get(self):
        x=100
        return {x}

class AudioCoding(Resource):
    def get(self):

        return {'VideoCoding': 'file:///C:/Users/nuriaestaras/Desktop/jordi/provahtml.html'}


api.add_resource(Menu, '/')
api.add_resource(VideoCoding, '/1')
api.add_resource(AudioCoding, '/2')

if __name__ == '__main__':
    app.run(debug=True)