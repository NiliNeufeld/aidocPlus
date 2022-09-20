from DAL.DB_repo import DBRepo


class MoviesRepo:

    def __init__(self, repo: DBRepo) -> None:
        self.repo = repo
