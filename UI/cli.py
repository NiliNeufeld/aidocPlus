from BL.library import *
import click


@click.group()
def main():
    pass


@main.command()
@click.option('--movie_name', '-mn', prompt=True, help="Name of the movie", required=True)
@click.option('--description', '-d', prompt=True, help="Description of the movie", required=True)
@click.option('--score', '-s', type=click.IntRange(1, 5), help="Movie's critic score", required=False)
def create_movie_request(movie_name: str, description: str, score: int):
    if len(movie_name) < 2:
        print("movie name must contain at least 2 characters")
        return
    if len(description) < 10:
        print("movie description must contain at least 10 characters")
        return
    library = Library()
    cmc = CreateMovieCommand(movie_name, description, score)
    new_movie: Movie = library.add_movie(cmc)
    print(new_movie)


@main.command()
def get_latest_movies_request() -> list:
    library = Library()
    movies = library.get_latest_movies()
    if movies is None:
        print("movies library is empty")
    else:
        for i, movie in zip(range(NUMBER_OF_MOVIES), movies):
            print(i+1, movie.name)
        return movies


@main.command()
@click.option('--movie_id', '-mid', prompt=True, help="movie id", required=True)
def get_movie_request(movie_id: int):
    library = Library()
    movie = library.get_movie(movie_id)
    if movie is None:
        print("movie id does not exist")
    else:
        print(movie)


