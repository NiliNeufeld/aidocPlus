from UI.api import app
from unittest import TestCase
from startup.dependecies import library
from tests.integration.add_ons_for_tests import MovieTest, JSON_VALID_MOVIE_TEST, JSON_INVALID_MOVIE_TEST
import json


class TestPostMovie(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def tearDown(self):
        library.delete_all_movies()

    def test_post_movie_with_valid_input_expect_response_200(self):
        response = self.app.post('/movie', json=JSON_VALID_MOVIE_TEST)
        assert response.status_code == 200
        j = json.loads(response.data)
        movie = MovieTest(**j)
        assert vars(movie) == JSON_VALID_MOVIE_TEST

    def test_post_movie_with_invalid_input_expect_response_400(self):
        response = self.app.post('/movie', json=JSON_INVALID_MOVIE_TEST)
        assert response.status_code == 400