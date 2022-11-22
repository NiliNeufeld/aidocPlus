from BL.library import Library
from DAL.DB_repo import DBRepo
from DAL.DB_handler import DBHandler
from DAL.json_repo import JsonRepo
from DAL.DB_sqlalchemy_repo import DBSQLAlchemyRepo
from BL.validations import Validations
import os

working_dir = os.getcwd()
DB_LOCATION = working_dir + "\\DAL\\aidoc_plus.db"
JSON_LOCATION = working_dir + "\\DAL\\aidoc_plus.json"

val = Validations()
repo_options = {'json': False, 'sqlite_repo': False, 'sqlalchemy_repo': True}
if repo_options['json'] is True:
    repo = JsonRepo(JSON_LOCATION)
else:
    if repo_options['sqlite_repo'] is True:
        repo = DBRepo(DBHandler(DB_LOCATION))
        repo.create_movies_table()
    else:
        repo = DBSQLAlchemyRepo()
library = Library(repo, val)


