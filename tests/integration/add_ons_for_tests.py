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
