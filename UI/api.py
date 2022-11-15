from flask import Flask, jsonify, request
from flask_restx import Resource, Api, reqparse, inputs
from BL.create_movie_command import CreateMovieCommand
from startup.dependecies import library
import UI.validations as validate
from common.movie import Movie
from common.movie_summary import MovieSummary
from typing import List


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


# @api.route('/movie')
# class Movie(Resource):
#     @api.doc(parser=new_movie_parser)
#     def post(self):
#         args = new_movie_parser.parse_args()
#         cmc = CreateMovieCommand(args['name'], args['description'], args['score'])
#         if not new_movie_validation(cmc):
#             return "values didn't pass validation, try again", 400
#         new_movie = library.add_movie(cmc)
#         return jsonify(new_movie.__dict__)

@api.route('/movie')
class Movie(Resource):
    def post(self) -> Movie:
        request_data = request.get_json()
        if not validate.presence_of_all_fields_new_movie(request_data):
            return "values didn't pass validation, try again", 400
        cmc = CreateMovieCommand(request_data['name'], request_data['description'], request_data['score'])
        if not validate.new_movie_fields(cmc):
            return "values didn't pass validation, try again", 400
        new_movie = library.add_movie(cmc)
        return jsonify(new_movie.__dict__)


@api.route('/movie/<string:movie_id>')
class Movie(Resource):
    def get(self, movie_id: str) -> Movie:
        new_movie = library.get_movie(movie_id)
        if new_movie is None:
            return "movie id doesn't exist in DB"
        return jsonify(new_movie.__dict__)

    def delete(self, movie_id: str):
        if not library.delete_movie(movie_id):
            return "movie id doesn't exist in DB"
        return "movie id"+movie_id+" deleted", 200


@api.route('/latestMovies')
class Movie(Resource):
    @api.doc(parser=latest_movies_parser)
    def get(self) -> List[MovieSummary]:
        args = latest_movies_parser.parse_args()
        movies = library.get_latest_movies(args['latestMovies'])
        if movies is None:
            return None
        else:
            return jsonify([obj.__dict__ for obj in movies])


@api.route('/searchMovie')
class Movie(Resource):
    @api.doc(parser=search_movies_parser)
    def get(self) -> List[MovieSummary]:
        args = search_movies_parser.parse_args()
        try:
            search_results = library.search_movie(args['searchValue'])
        except ValueError:
            return "the search value didn't pass validation, try again", 400
        else:
            if search_results is None:
                return None
            return jsonify([obj.__dict__ for obj in search_results])