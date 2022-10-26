from BL.create_movie_command import CreateMovieCommand
import click
from UI.dependecies import library, val


@click.group()
def main_menu():
    pass


@main_menu.command()
@click.option('--movie_name', '-mn', prompt=True, help="Name of the movie", required=True)
@click.option('--description', '-d', prompt=True, help="Description of the movie", required=True)
@click.option('--score', '-s', type=click.IntRange(1, 5), help="Movie's critic score", required=False)
def create_movie_request(movie_name: str, description: str, score: int):
    while len(movie_name) < 2:
        print("movie name must contain at least 2 characters")
        movie_name = click.prompt('Please enter a valid movie name')
    while len(description) < 10:
        print("movie description must contain at least 10 characters")
        description = click.prompt('Please enter a valid movie description')
    cmc = CreateMovieCommand(movie_name, description, score)
    new_movie = library.add_movie(cmc)
    print(new_movie)


@main_menu.command()
@click.option('--number_of_movies', '-m', type=click.IntRange(1, ), prompt=True, help="latest movies", required=True)
def get_latest_movies_request(number_of_movies: int):
    movies = library.get_latest_movies(number_of_movies)
    if movies is None:
        print("movies library is empty")
    else:
        for i, movie in zip(range(number_of_movies), movies):
            print(i+1, ":", movie.name)
        movie_number = input("which movie would you like to watch:")
        while int(movie_number) > number_of_movies or int(movie_number) < 1:
            print("the number you entered is out of list range")
            movie_number = input("which movie would you like to watch:")
        else:
            movie = library.get_movie(movies[int(movie_number)-1].mid)
            print(movie)

# @main_menu.command()
# @click.option('--movie_number', '-m', type=click.IntRange(1, ), prompt=True, help="movie id", required=True)
# def get_movie_request(movie_number: int):
#     movie = library.get_movie(movie_number)
#     if movie is None:
#         click.echo("movie does not exist")
#     else:
#         click.echo(movie)


@main_menu.command()
@click.option('--search_value', '-s',  prompt=True, help="search", required=True)
def search_request(search_value: str):
    while not val.search_validation(search_value):
        search_value = click.prompt(
            "please enter a search string longer than two characters and without any digits")
    try:
        search_results = library.search_movie(search_value)
    except ValueError as ve:
        print(ve)
    else:
        if search_results is None:
            print("No matched results were found")
        else:
            for i, movie in zip(range(len(search_results)), search_results):
                print(i+1, ":", movie.name)

