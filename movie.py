from datetime import datetime
import uuid


class Movie:
    def __init__(self, name, description, score, mid=0, date=0):
        if mid == 0:
            self.mid = uuid.uuid4()
        else:
            self.mid = mid
        self.name = name
        self.description = description
        self.score = score
        if date == 0:
            self.date = datetime.now()
        else:
            self.date = date

    def __str__(self):
        return "Movie name: % s\n" \
               "Description: % s\n" \
               "Critic score: % s\n" \
               "Date added: % s" % (self.name, self.description, self.score, self.date.strftime('%m/%d/%Y'))




