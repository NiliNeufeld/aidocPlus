import uuid


class MovieSummary:
    def __init__(self, name: str, mid=0):
        if mid == 0:
            self.mid = uuid.uuid4()
        else:
            self.mid = mid
        self.name = name





