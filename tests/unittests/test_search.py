import unittest
from unittest.mock import Mock
from BL.library import Library
from BL.validations import Validations
from DAL.movies_repo import MoviesRepo
from common.movie_summary import MovieSummary


class TestSearchBL(unittest.TestCase):

    def setUp(self) -> None:
        self.val = Mock(spec=Validations)
        self.movie_repo = Mock(spec=MoviesRepo)
        self.library = Library(self.movie_repo, self.val)

    def test_valid_input_movies_found(self):
        # Arrange
        str0 = "bl"
        movie_summary1 = MovieSummary("bla")
        movie_summary2 = MovieSummary("bla")
        movies_list = [movie_summary1, movie_summary2]
        self.movie_repo.search_movies.return_value = movies_list

        # Act
        output = self.library.search_movie(str0)

        # Assert
        self.assertEqual(movies_list, output)

    def test_valid_input_movies_not_found(self):
        # Arrange
        str1 = "abc"
        self.movie_repo.search_movies.return_value = None

        # Act
        output = self.library.search_movie(str1)

        # Assert
        self.assertEqual(None, output)

    def test_raise_for_invalid_input(self):
        # Arrange
        str1 = "ab"
        # self.movie_repo.search_movies.return_value = ValueError
        self.val.search_validation.return_value = False
        # Act+Assert
        with self.assertRaises(ValueError):
            self.library.search_movie(str1)


class TestSearchDAL(unittest.TestCase):

    def setUp(self) -> None:
        self.val = Mock(spec=Validations)
        self.movie_repo = Mock(spec=MoviesRepo)
        self.library = Library(self.movie_repo, self.val)

    def test_valid_input_movies_found(self):
        # Arrange
        str0 = "bl"
        movie_summary1 = MovieSummary("bla")
        movie_summary2 = MovieSummary("bla")
        movies_list = [movie_summary1, movie_summary2]
        self.movie_repo.search_movies.return_value = movies_list

        # Act
        output = self.library.search_movie(str0)

        # Assert
        self.assertEqual(movies_list, output)

    def test_valid_input_movies_not_found(self):
        # Arrange
        str1 = "abc"
        self.movie_repo.search_movies.return_value = None

        # Act
        output = self.library.search_movie(str1)

        # Assert
        self.assertEqual(None, output)

    def test_raise_for_invalid_input(self):
        # Arrange
        str1 = "ab"
        # self.movie_repo.search_movies.return_value = ValueError
        self.val.search_validation.return_value = False
        # Act+Assert
        with self.assertRaises(ValueError):
            self.library.search_movie(str1)