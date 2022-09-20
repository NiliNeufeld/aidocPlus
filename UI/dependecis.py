# import UI.cli as cli
import UI.clinew as cli
from BL.library import Library
from DAL.movies_repo import MoviesRepo
from DAL.DB_repo import DBRepo
from DAL.DB_handler import DBHandler
import os

DB_LOCATION = os.path.dirname(os.path.abspath(__file__)) + "\\aidoc_plus.db"

library = Library(
    repo=MoviesRepo(
        repo=DBRepo(
            db_handler=DBHandler(DB_LOCATION)
        )
    )
)