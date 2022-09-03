import json
import movie
from datetime import datetime
import os

directory = os.path.dirname(os.path.abspath(__file__))


class JsonRepo:
    def __init__(self):
        self.movies_list = []
        with open(directory + "\data.json") as f: # TODO: add try-catch
            movies_library = json.load(f)
            f.close()
        for item in movies_library:
            m = movie.Movie(item["name"], item["description"], item["score"],
                            item["mid"], datetime.strptime(item["date"], "%Y-%m-%d %H:%M:%S.%f"))
            self.movies_list.append(m)

    def add_movie(self, new_movie):
        self.movies_list.append(new_movie)
        f = open(directory + "\data.json", "w") # TODO: add try-catch
        f.write(json.dumps([m.__dict__ for m in self.movies_list], default=str, indent=4))
        f.close()