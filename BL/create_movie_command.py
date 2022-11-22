class CreateMovieCommand:
    def __init__(self, name, description, score=None):
        self.name = name
        self.description = description
        self.score = score