from BL.library import Library
from DAL.movies_repo import MoviesRepo
from DAL.DB_repo import DBRepo
from DAL.DB_handler import DBHandler
from DAL.json_repo import JsonRepo
import os

working_dir = os.getcwd()
DB_LOCATION = working_dir + "\\DAL\\aidoc_plus.db"
JSON_LOCATION = working_dir + "\\DAL\\aidoc_plus.json"

should_use_db_repo = False
repo = DBRepo(DBHandler(DB_LOCATION)) if should_use_db_repo else JsonRepo(JSON_LOCATION)
library = Library(repo)


