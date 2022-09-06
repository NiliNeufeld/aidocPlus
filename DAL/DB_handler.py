from sqlite3 import Error
import sqlite3


class DBHandler:

    def __init__(self, db_location: str) -> None:
        try:
            self.connection = sqlite3.connect(db_location, detect_types=sqlite3.PARSE_DECLTYPES)
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

    # def get_tables(self) -> None:
    #     self.cur.execute("SELECT name FROM sqlite_master WHERE type='table';")
    #     print(self.cur.fetchall())