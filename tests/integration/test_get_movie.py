from UI.api import app
from unittest import TestCase
from startup.dependecies import library
from tests.integration.add_ons_for_tests import MovieTest, JSON_VALID_MOVIE_TEST
import json
import uuid


class TestGetMovie(TestCase):
    def setUp(self):
        self.app = app.test_client()
        library.delete_all_movies()

    def tearDown(self):
        library.delete_all_movies()

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