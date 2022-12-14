import click
from library import *


@click.group()
def main():
    pass


@main.command()
@click.option('--movie_name', '-mn', prompt=True, help="Name of the movie", required=True)
@click.option('--description', '-d', prompt=True, help="Description of the movie", required=True)
@click.option('--score', '-s', type=click.IntRange(1, 5), help="Movie's critic score", required=False)
# read about difference between option / argument
def add_new_movie(movie_name, description, score):
    if len(movie_name) < 2:
        raise ValueError("movie name must be at least 2 characters")
    if len(description) < 10:
        raise ValueError("movie description must be at least 10 characters")
    library = Library()
    new_movie = Movie(0, movie_name, description, score, 0, library)
    library.add_movie(new_movie)
    print(new_movie)


@main.command()
def get_latest_5_movies():
    library = Library()
    movies = library.get_latest_5()
    for i, movie in zip(range(5), movies):
        print(i+1, movie.name)


@main.command()
@click.option('--movie_id', '-mid', prompt=True, help="movie id", required=True)
def get_movie_details(movie_id):
    library = Library()
    movie = library.get_movie(int(movie_id))
    print(movie)


if __name__ == '__main__':
    main()