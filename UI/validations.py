from BL.create_movie_command import CreateMovieCommand as cmc


def new_movie_validation(movie: cmc) -> bool:
    if len(movie.name) < 2 or len(movie.description) < 10:
        return False
    return True
