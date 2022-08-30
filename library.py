import json
from movie import *

NUMBER_OF_MOVIES = 5


class Library:
    def __init__(self):
        self.movies_list = []
        with open('data.json') as f:
            movies_library = json.load(f)
            f.close()
        for movie in movies_library:
            m = Movie(movie["name"], movie["description"], movie["score"], datetime.strptime(movie["date"], "%Y-%m-%d %H:%M:%S.%f"), movie["mid"])
            self.movies_list.append(m)

    def add_movie(self, movie):
        self.movies_list.append(movie)
        f = open("data.json", "w")
        f.write(json.dumps([m.__dict__ for m in self.movies_list], default=str, indent=4))
        f.close()

    def get_latest_movies(self):
        sorted_by_date = sorted(self.movies_list, key=lambda x: x.date, reverse=True)
        # check,seems like sorting by isn't working
        # for it in sorted_by_date:
        #     print(it, "\n")
        return sorted_by_date[:NUMBER_OF_MOVIES]

    def get_movie(self, movie_id):
        return next(x for x in self.movies_list if x.mid == movie_id)