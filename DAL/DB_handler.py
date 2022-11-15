from sqlite3 import Error
import sqlite3


class DBHandler:

    def __init__(self, db_location: str):
        self.db_location = db_location
        self.connection = None
        self.cur = None

    def connect(self) -> None:
        try:
            self.connection = sqlite3.connect(self.db_location, detect_types=sqlite3.PARSE_DECLTYPES)
            self.cur = self.connection.cursor()
        except Error as e:
            print(e)
            self.connection = None
            self.cur = None

    def close(self) -> None:
        self.connection.close()

    def execute(self, sql: str, new_data: object) -> None:
        self.cur.execute(sql, new_data)

    def commit(self) -> None:
        self.connection.commit()