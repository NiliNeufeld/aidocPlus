from UI.api import app
from unittest import TestCase
from startup.dependecies import library
from tests.integration.add_ons_for_tests import MovieSummaryTest, JSON_VALID_MOVIE_TEST
import json


class TestSearchMovies(TestCase):
    def setUp(self):
        self.app = app.test_client()
        library.delete_all_movies()

    def tearDown(self):
        library.delete_all_movies()

    def test_get_search_movies_insert_new_movies_and_expect_getting_them_and_response_200(self):
        response1 = self.app.post('/movie', json=JSON_VALID_MOVIE_TEST)
        response2 = self.app.post('/movie', json=JSON_VALID_MOVIE_TEST)
        assert response1.status_code == 200
        assert response2.status_code == 200
        response = self.app.get('/searchMovie?searchValue=test')
        assert response.status_code == 200
        j = json.loads(response.data)
        movie1 = MovieSummaryTest(**j[0])
        movie2 = MovieSummaryTest(**j[1])
        assert movie1.name == JSON_VALID_MOVIE_TEST['name']
        assert movie2.name == JSON_VALID_MOVIE_TEST['name']

    def test_get_search_movies_when_no_results_are_found_expect_response_200_and_NONE(self):
        response = self.app.get('/searchMovie?searchValue=movie_that_does_not_exist_in_DB')
        assert response.status_code == 200
        assert response.json is None

    def test_get_search_movies_with_invalid_search_value_expect_response_400(self):
        response = self.app.get('/searchMovie?searchValue=s')
        assert response.status_code == 400
        assert response.json == "the search value didn't pass validation, try again"