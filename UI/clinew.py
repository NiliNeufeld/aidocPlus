from BL.library import Library
from BL.create_movie_command import CreateMovieCommand
import click
from UI.dependecis import library


@click.group()
# @click.pass_context
def main_menu():
    pass

# x = None

# @click.group()
# @click.pass_context
# def main_menu(*args): #lib,
    # lib.obj =library
    # x = args[0]
    # pass


@main_menu.command()
@click.option('--movie_name', '-mn', prompt=True, help="Name of the movie", required=True)
@click.option('--description', '-d', prompt=True, help="Description of the movie", required=True)
@click.option('--score', '-s', type=click.IntRange(1, 5), help="Movie's critic score", required=False)
def create_movie_request(movie_name: str, description: str, score: int):
    # print("create_movie_request")
    while len(movie_name) < 2:
        print("movie name must contain at least 2 characters")
        movie_name = click.prompt('Please enter a valid movie name')
    while len(description) < 10:
        print("movie description must contain at least 10 characters")
        movie_name = click.prompt('Please enter a valid movie description')
    cmc = CreateMovieCommand(movie_name, description, score)
    new_movie = library.add_movie(cmc)
    # ctx.obj['lib']
    print(new_movie)


@main_menu.command()
@click.option('--number_of_movies', '-m', type=click.IntRange(1, ), prompt=True, help="movie id", required=True)
def get_latest_movies_request(number_of_movies: int) -> list:
    print("get_latest_movies_request")
    movies = library.get_latest_movies(number_of_movies)
    if movies is None:
        print("movies library is empty")
    else:
        for i, movie in zip(range(number_of_movies), movies):
            print(i+1, movie.name)
        return movies


@main_menu.command()
@click.option('--movie_number', '-m', type=click.IntRange(1, ), prompt=True, help="movie id", required=True)
def get_movie_request(movie_number: int):
    print("get_movie_request")
    movie = library.get_movie(movie_number)
    if movie is None:
        print("movie does not exist")
    else:
        print(movie)

