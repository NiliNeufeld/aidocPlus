import datetime


class Movie:
    def __init__(self, name: str, description: str, score: int, date: datetime, mid):
        self.mid = mid
        self.name = name
        self.description = description
        self.score = score
        self.date = date

    def __str__(self) -> str:
        return "Movie name: % s\n" \
               "Description: % s\n" \
               "Critic score: % s\n" \
               "Date added: % s" % (self.name, self.description, self.score, self.date.strftime('%m/%d/%Y'))




