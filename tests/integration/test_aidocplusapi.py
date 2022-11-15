from UI.api import app
from unittest import TestCase
from startup.dependecies import library
import json
import uuid

JSON_VALID_MOVIE_TEST = {
    "name": "test movie",
    "description": "this is a test movie",
    "score": 5
}

JSON_INVALID_MOVIE_TEST = {
    "description": "this is a test movie",
    "score": 5
}


class MovieTest:
    def __init__(self, name, description, score=None, date=None, mid=None):
        self.name = name
        self.description = description
        self.score = score


class MovieSummaryTest:
    def __init__(self, name, mid):
        self.name = name
        self.mid = mid


class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()
        library.delete_all_movies()

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

    def test_get_movie_with_valid_id_expect_response_200(self):
        response1 = self.app.post('/movie', json=JSON_VALID_MOVIE_TEST)
        json_data1 = json.loads(response1.data)
        response2 = self.app.get('/movie/'+json_data1['mid'])
        assert response2.status_code == 200
        j = json.loads(response2.data)
        movie = MovieTest(**j)
        assert vars(movie) == JSON_VALID_MOVIE_TEST

    def test_get_movie_with_non_existing_id_expect_response_404(self):
        movie_id = uuid.uuid4()
        response = self.app.get('/movie/'+str(movie_id))
        assert response.status_code == 200

    def test_get_latest_movies_insert_new_movies_and_expect_getting_them_and_response_200(self):
        response1 = self.app.post('/movie', json=JSON_VALID_MOVIE_TEST)
        response2 = self.app.post('/movie', json=JSON_VALID_MOVIE_TEST)
        assert response1.status_code == 200
        assert response2.status_code == 200
        response = self.app.get('/latestMovies?latestMovies=2')
        assert response.status_code == 200
        j = json.loads(response.data)
        movie1 = MovieSummaryTest(**j[0])
        movie2 = MovieSummaryTest(**j[1])
        assert movie1.name == JSON_VALID_MOVIE_TEST['name']
        assert movie2.name == JSON_VALID_MOVIE_TEST['name']

    def test_get_latest_movies_with_empty_db_expect_response_200_and_NONE(self):
        response = self.app.get('/latestMovies?latestMovies=2')
        assert response.status_code == 200
        assert response.json is None

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

    def test_delete_with_existing_ID_expect_response_200(self):
        response1 = self.app.post('/movie', json=JSON_VALID_MOVIE_TEST)
        assert response1.status_code == 200
        new_movie_id = json.loads(response1.data)['mid']
        response = self.app.delete('/movie/' + new_movie_id)
        assert response.status_code == 200
        assert response.json == "movie id"+new_movie_id+" deleted"

    def test_delete_with_non_existing_ID_expect_response_200(self):
        movie_id = uuid.uuid4()
        response = self.app.delete('/movie/' + str(movie_id))
        assert response.status_code == 200
        assert response.json == "movie id doesn't exist in DB"