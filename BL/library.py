from DAL.repo import *
from movie import *

NUMBER_OF_MOVIES = 5


class Library:
    def __init__(self):
        self._repo = JsonRepo()

    def add_movie(self, cmc):
        new_movie = Movie(cmc.name, cmc.description, cmc.score)
        self._repo.add_movie(new_movie)
        return new_movie

    def get_latest_movies(self):
        sorted_by_date = sorted(self._repo.movies_list, key=lambda x: x.date, reverse=True)
        return sorted_by_date[:NUMBER_OF_MOVIES]

    def get_movie(self, movie_id): # TODO: handle unfounded id
        return next(x for x in self._repo.movies_list if x.mid == movie_id)
