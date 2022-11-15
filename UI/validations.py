from BL.create_movie_command import CreateMovieCommand as cmc


def presence_of_all_fields_new_movie(movie_data: dict) -> bool:
    return all([movie_data.get('name', False), movie_data.get('description', False)])


def new_movie_fields(movie: cmc) -> bool:
    if len(movie.name) < 2 or len(movie.description) < 10:
        return False
    return True
