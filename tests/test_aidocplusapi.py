from UI.aidocPlusAPI import app
from unittest import TestCase
import json


class TestIntegrations(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_post_movie_200(self):
        response = self.app.post('/movie?name=test_movie&description=this_is_a_test_movie&score=5')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data['name'] == 'test_movie'
        assert json_data['score'] == 5
        assert json_data['description'] == 'this_is_a_test_movie'

    def test_post_invalid_movie_400_invalid(self):
        response = self.app.post('/movie?description=this%20is%20a%20valid%20movie&score=5')
        assert response.status_code == 400

    def test_post_movie_200(self):
        response = self.app.post('/movie?name=test_movie&description=this_is_a_test_movie&score=5')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data['name'] == 'test_movie'
        assert json_data['score'] == 5
        assert json_data['description'] == 'this_is_a_test_movie'

    def test_post_invalid_movie_400_invalid(self):
        response = self.app.post('/movie?description=this%20is%20a%20valid%20movie&score=5')
        assert response.status_code == 400
