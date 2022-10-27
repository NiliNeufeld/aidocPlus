from DAL.movies_repo import MoviesRepo
from BL.create_movie_command import CreateMovieCommand
from BL.validations import Validations
from common.movie import Movie
from common.movie_summary import MovieSummary
import datetime
import uuid
from typing import List


class Library:
    def __init__(self, repo: MoviesRepo, val: Validations):
        self._repo = repo
        self.val = val

    def add_movie(self, cmc: CreateMovieCommand) -> Movie:
        new_movie = Movie(cmc.name, cmc.description, cmc.score, datetime.datetime.now(datetime.timezone.utc), uuid.uuid4())
        self._repo.add_movie(new_movie)
        return new_movie

    def get_latest_movies(self, number_of_movies: int) -> List[MovieSummary]:
        return self._repo.get_latest_movies(number_of_movies)

    def get_movie(self, movie_id: str) -> Movie:
        return self._repo.get_movie_id(movie_id)

    def search_movie(self, search_value: str) -> List[MovieSummary]:
        if not self.val.search_validation(search_value):
            raise ValueError("please enter a search string longer than two characters and without any digits")

        return self._repo.search_movies(search_value)



