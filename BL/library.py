from DAL.repo import *
from BL.create_movie_command import CreateMovieCommand
from common.movie import *
import datetime


class Library:
    def __init__(self) -> None:
        self._repo = JsonRepo()

    def add_movie(self, cmc: CreateMovieCommand) -> Movie:
        new_movie = Movie(cmc.name, cmc.description, cmc.score, datetime.datetime.now(datetime.timezone.utc))
        self._repo.add_movie(new_movie)
        return new_movie

    def get_latest_movies(self) -> list:
        return self._repo.get_latest_movies()

    def get_movie(self, movie_id: int) -> Movie:
        latest_movies = self._repo.get_latest_movies()
        if movie_id > len(latest_movies):
            return None
        else:
            return latest_movies[movie_id-1]
