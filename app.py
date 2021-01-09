
from flask import Flask
from flask_restful import Resource, Api, reqparse
import werkzeug
import pafy
import lxml
from lxml import etree

app = Flask(__name__)
api = Api(app)

class Menu(Resource):
    def get(self):

        return {'Menu': 'use /VideoDuration to get some especifications of a video from youtube, /Diagram to see the perceptual coder diagram'}

class VideoCodingExplication(Resource):
    def get(self):

        return {'Explication': 'add to the url /id where id is the identifier of a youtube video. For example from the youtube video https://www.youtube.com/watch?v=gORX2ww5hxU the identifier is: gORX2ww5hxU, what comes after the =.'}

class VideoCoding(Resource):
    def get(self, id):
        
        url = 'https://www.youtube.com/watch?v=' + id
        
        video = pafy.new(url)
        s = video.getbest()
        a=video.getbestaudio()
        return {'video': {'title':video.title , 'duration': video.length , 'best resolution': s.resolution, ' extension' : s.extension, 'audio extension':a.extension}}, 200

class AudioCoding(Resource):
    def get(self):

        return {'Diagram': 'https://github.com/Jordimuletestaras/API/blob/main/diagrama.JPG'}


api.add_resource(Menu, '/')
api.add_resource(VideoCodingExplication, '/VideoDuration')
api.add_resource(VideoCoding, '/VideoDuration/<string:id>')
api.add_resource(AudioCoding, '/Diagram')

if __name__ == '__main__':
    app.run(debug=True)