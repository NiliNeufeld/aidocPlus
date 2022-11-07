from flask import Flask
from flask_restx import Resource, Api, reqparse

from BL.create_movie_command import CreateMovieCommand
from UI.dependecies import library

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('name', type=str, help='movie name')
parser.add_argument('description', type=str, help='movie description')
parser.add_argument('score', type=int, help='movie score')


@api.route('/movie')
class Movie(Resource):
    @api.doc(parser=parser)
    def post(self):
        args = parser.parse_args()
        cmc = CreateMovieCommand(args['name'], args['description'], args['score'])
        new_movie = library.add_movie(cmc)
        return f"new movie:{new_movie}"




# @api.route('/hello')
# class HelloWorld(Resource):
#     def get(self):
#         return {'hello': 'world'}
#
# @app.route("/create_movie/<string:todo_id>'")
# class CreateMovie(Resource):
#     def post(self):
#         # TODO - validation
#         # TODO - handle errors
#         cmc = CreateMovieCommand(movie_name, description, score)
#         new_movie = library.add_movie(cmc)
#         print(new_movie)
#         # client = Client()
#         # data = client.get_scans()
#         # if isinstance(data, int):
#         #     return "status code:"+str(data)
#         # elif not data:
#         #     return "no scans data was sent from aidoc server"
#         # else:
#         #     groupbyCategory = request.args.get("groupby")
#         #     scans = group_by(groupbyCategory, data)
#         #     return scans
#
#
# @app.route("/get_latest_movies_request")
# def get_latest_movies_request():

#
# @app.route("/create_movie")
# def create_movie_request():

