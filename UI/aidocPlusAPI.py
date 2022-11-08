from flask import Flask, Response
from flask_restx import Resource, Api, reqparse, inputs

from BL.create_movie_command import CreateMovieCommand
from UI.dependecies import library
from UI.validations import new_movie_validation
import json

app = Flask(__name__)
api = Api(app)


new_movie_parser = reqparse.RequestParser()
new_movie_parser.add_argument('name', type=str, help='movie name', required=True)
new_movie_parser.add_argument('description', type=str, help='movie description', required=True)
new_movie_parser.add_argument('score', type=inputs.int_range(1, 5), help='movie score')

latest_movies_parser = reqparse.RequestParser()
latest_movies_parser.add_argument('latestMovies', type=int, help='get the latest X movies in aidocPlus', required=True)

search_movies_parser = reqparse.RequestParser()
search_movies_parser.add_argument('searchValue', type=str, help='find movies containing this string', required=True)


@api.route('/movie')
class Movie(Resource):
    @api.doc(parser=new_movie_parser)
    def post(self):
        args = new_movie_parser.parse_args()
        cmc = CreateMovieCommand(args['name'], args['description'], args['score'])
        if not new_movie_validation(cmc):
            return "values didn't pass validation, try again", 400
        new_movie = library.add_movie(cmc)
        return json.dumps(new_movie.__dict__, sort_keys=True, default=str)


@api.route('/movie/<string:movie_id>')
class Movie(Resource):
    def get(self, movie_id: str):
        new_movie = library.get_movie(movie_id)
        if new_movie is None:
            return "movie not found", 404
        return json.dumps(new_movie.__dict__, sort_keys=True, default=str)


@api.route('/latestMovies')
class Movie(Resource):
    @api.doc(parser=latest_movies_parser)
    def get(self):
        args = latest_movies_parser.parse_args()
        movies = library.get_latest_movies(args['latestMovies'])
        if movies is None:
            return None
        else:
            return json.dumps([obj.__dict__ for obj in movies], sort_keys=True, default=str)


@api.route('/searchMovie')
class Movie(Resource):
    @api.doc(parser=search_movies_parser)
    def get(self):
        args = search_movies_parser.parse_args()
        try:
            search_results = library.search_movie(args['searchValue'])
        except ValueError:
            return "the search value didn't pass validation, try again", 400
        else:
            if search_results is None:
                return None
            return json.dumps([obj.__dict__ for obj in search_results], sort_keys=True, default=str)