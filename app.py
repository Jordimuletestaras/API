
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

        return {'Menu': 'use /VideoDuration to get the duration of a video from youtube, /Diagram to see the perceptual coder diagram'}

class VideoCoding(Resource):
    def get(self, id):
        
        url = 'https://www.youtube.com/watch?v=' + id
        
        video = pafy.new(url)

        #youtube = etree.HTML(urllib.urlopen(url).read()) 
        #join(video_title)
        return {'video': {'title':'hhhh' , 'duration': video.length}}, 200

class AudioCoding(Resource):
    def get(self):

        return {'image': 'https://github.com/Jordimuletestaras/API/blob/main/diagrama.JPG'}


api.add_resource(Menu, '/')
api.add_resource(VideoCoding, '/VideoDuration/<string:id>')
api.add_resource(AudioCoding, '/Diagram')

if __name__ == '__main__':
    app.run(debug=True)