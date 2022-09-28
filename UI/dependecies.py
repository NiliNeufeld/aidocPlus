from BL.library import Library
from DAL.DB_repo import DBRepo
from DAL.DB_handler import DBHandler
from DAL.json_repo import JsonRepo
import os

working_dir = os.getcwd()
DB_LOCATION = working_dir + "\\DAL\\aidoc_plus.db"
JSON_LOCATION = working_dir + "\\DAL\\aidoc_plus.json"

should_use_db_repo = True
if should_use_db_repo:
    repo = DBRepo(DBHandler(DB_LOCATION))
    repo.create_movies_table()
else:
    repo = JsonRepo(JSON_LOCATION)
library = Library(repo)


