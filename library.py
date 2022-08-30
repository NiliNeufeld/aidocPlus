import repo
import movie

NUMBER_OF_MOVIES = 5


class Library:
    def __init__(self):
        self._repo = repo.load_json_repo()

    def add_movie(self, cmc):
        new_movie = movie.Movie()
        self._repo.append(new_movie)
        repo.update_json_repo(self._repo)

    def get_latest_movies(self):
        sorted_by_date = sorted(self._repo, key=lambda x: x.date, reverse=True)
        # check,seems like sorting by isn't working
        # for it in sorted_by_date:
        #     print(it, "\n")
        return sorted_by_date[:NUMBER_OF_MOVIES]

    def get_movie(self, movie_id):
        return next(x for x in self._repo if x.mid == movie_id)