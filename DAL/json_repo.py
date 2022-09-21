import json
from common.movie import *
from datetime import datetime
from DAL.movies_repo import MoviesRepo


class JsonRepo(MoviesRepo):
    def __init__(self, location: str):
        self.movies_list = []
        self.path = location

    def load_data(self) -> None:
        with open(self.path) as f:
            movies_library = json.load(f)
            f.close()
        for item in movies_library:
            m = Movie(item["name"], item["description"], item["score"],
                      datetime.strptime(item["date"], "%Y-%m-%d %H:%M:%S.%f%z"), item["mid"])
            self.movies_list.append(m)
            f.close()

    def update_data(self) -> None:
        f = open(self.path, "w")
        f.write(json.dumps([m.__dict__ for m in self.movies_list], default=str, indent=4))
        f.close()

    def add_movie(self, new_movie: Movie) -> None:
        self.load_data()
        self.movies_list.append(new_movie)
        self.update_data()

    def get_latest_movies(self, number_of_movies: int) -> list:
        self.load_data()
        if not self.movies_list:
            return None
        sorted_by_date = sorted(self.movies_list, key=lambda x: x.date, reverse=True)
        return sorted_by_date[:number_of_movies]

    def get_movie_id(self, movie_id: int) -> Movie:
        self.load_data()
        return next((x for x in self.movies_list if x.mid == movie_id), None)
