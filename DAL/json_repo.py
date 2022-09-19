import json
from common.movie import *
from datetime import datetime
import os

directory = os.path.dirname(os.path.abspath(__file__))
NUMBER_OF_MOVIES = 5


class JsonRepo:
    def __init__(self) -> None:
        self.movies_list = []
        with open(directory + "\data.json") as f:
            movies_library = json.load(f)
            f.close()
        for item in movies_library:
            m = Movie(item["name"], item["description"], item["score"],
                            datetime.strptime(item["date"], "%Y-%m-%d %H:%M:%S.%f%z"), item["mid"])
            self.movies_list.append(m)

    def add_movie(self, new_movie: Movie) -> None:
        self.movies_list.append(new_movie)
        f = open(directory + "\data.json", "w")
        f.write(json.dumps([m.__dict__ for m in self.movies_list], default=str, indent=4))
        f.close()

    def get_latest_movies(self) -> list:
        if not self.movies_list:
            return None
        sorted_by_date = sorted(self.movies_list, key=lambda x: x.date, reverse=True)
        return sorted_by_date[:NUMBER_OF_MOVIES]

    def get_movie_id(self, movie_id: int) -> Movie:
        return next((x for x in self.movies_list if x.mid == movie_id), None)