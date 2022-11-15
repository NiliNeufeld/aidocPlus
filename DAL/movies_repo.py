from abc import ABC, abstractmethod
from common.movie import Movie


class MoviesRepo(ABC):

    @abstractmethod
    def add_movie(self, movie: Movie):
        pass

    @abstractmethod
    def get_latest_movies(self, number_of_movies: int):
        pass

    @abstractmethod
    def get_movie_id(self, movie_id: str):
        pass

    @abstractmethod
    def search_movies(self, value: str):
        pass

    @abstractmethod
    def delete_movie(self, movie_id: str):
        pass

    @abstractmethod
    def delete_all_movies(self):
        pass
