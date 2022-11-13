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

    def test_post_movie_400(self):
        response = self.app.post('/movie?description=this%20is%20a%20valid%20movie&score=5')
        assert response.status_code == 400

    def test_get_movie_200(self):
        response = self.app.get('/movie/768f15dd-5280-43e2-9f6f-4ccb6985364a')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data == {
            "date": "Sun, 13 Nov 2022 14:50:47 GMT",
            "description": "this_is_a_valid_movie",
            "mid": "768f15dd-5280-43e2-9f6f-4ccb6985364a",
            "name": "valid_movie",
            "score": 5
        }

    def test_get_movie_404(self):
        response = self.app.get('/movie/76')
        assert response.status_code == 404
        assert response.json == "movie not found"

    def test_get_latest_movies_200(self):
        response1 = self.app.post('/movie?name=test_latest_movie1&description=this_is_a_test_movie&score=5')
        assert response1.status_code == 200
        response2 = self.app.post('/movie?name=test_latest_movie2&description=this_is_a_test_movie&score=5')
        assert response2.status_code == 200
        response = self.app.get('/latestMovies?latestMovies=2')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data[0]['name'] == 'test_latest_movie2'
        assert json_data[1]['name'] == 'test_latest_movie1'

    def test_get_latest_movies_NONE(self): # ask: how should I test the None response? (DB is empty)
        response = self.app.get('/latestMovies?latestMovies=0')
        assert response.status_code == 200
        assert response.json is None

    def test_get_search_movies_200(self):
        response1 = self.app.post('/movie?name=search_movie1&description=this_is_a_test_movie&score=5')
        assert response1.status_code == 200
        response2 = self.app.post('/movie?name=search_movie2&description=this_is_a_test_movie&score=5')
        assert response1.status_code == 200
        response = self.app.get('/searchMovie?searchValue=search_movie')
        assert response.status_code == 200
        json_data = json.loads(response.data)
        assert json_data[0]['name'] == 'search_movie1'
        assert json_data[1]['name'] == 'search_movie2'

    def test_get_search_movies_400(self):
        response = self.app.get('/searchMovie?searchValue=s')
        assert response.status_code == 400
        assert response.json == "the search value didn't pass validation, try again"