from DAL.DB_repo import DBRepo
from BL.create_movie_command import CreateMovieCommand
from common.movie import Movie
import datetime

# NUMBER_OF_MOVIES = 5


class Library:
    def __init__(self) -> None:  # , repo
        self._repo = DBRepo()
        self._repo.create_movies_table()

    def add_movie(self, cmc: CreateMovieCommand) -> Movie:
        new_movie = Movie(cmc.name, cmc.description, cmc.score, datetime.datetime.now(datetime.timezone.utc))
        self._repo.add_movie(new_movie)
        return new_movie

    def get_latest_movies(self, number_of_movies: int) -> list:
        return self._repo.get_latest_movies(number_of_movies)

    def get_movie(self, movie_id: int) -> Movie:
        latest_movies = self._repo.get_latest_movies(movie_id)
        if latest_movies is None or movie_id > len(latest_movies):
            return None
        else:
            return latest_movies[movie_id-1]
