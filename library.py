import json
from movie import *


class Library:
    def __init__(self):
        self.movies_list = []
        with open('data.json') as f:
            movies_library = json.load(f)
            f.close()
        for movie in movies_library:
            m = Movie(movie["mid"], movie["name"], movie["description"], movie["score"], datetime.strptime(movie["date"], "%Y-%m-%d %H:%M:%S.%f"), 0)
            self.movies_list.append(m)

    def add_movie(self, movie):
        # maybe it's not the best practice to read the whole file into a variable,
        # but I though it's betten then writing to the end of the file
        self.movies_list.append(movie)
        f = open("data.json", "w")
        f.write(json.dumps([m.__dict__ for m in self.movies_list], default=str, indent=4))
        f.close()

    def get_latest_5(self):
        return self.movies_list[-5:]

    def get_movie(self, movie_id):
        return self.movies_list[movie_id-1]