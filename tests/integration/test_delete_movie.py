from UI.api import app
from unittest import TestCase
from startup.dependecies import library
from tests.integration.add_ons_for_tests import JSON_VALID_MOVIE_TEST
import json
import uuid


class TestDeleteMovie(TestCase):
    def setUp(self):
        self.app = app.test_client()
        library.delete_all_movies()

    def tearDown(self):
        library.delete_all_movies()

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