from common.movie import Movie
from DAL.DB_handler import DBHandler
from datetime import datetime
# from BL.library import NUMBER_OF_MOVIES
import os

DB_LOCATION = os.path.dirname(os.path.abspath(__file__)) + "\\aidoc_plus.db"


class DBRepo:

    def __init__(self) -> None:
        self.DB = DBHandler(DB_LOCATION)

    def create_movies_table(self):
        self.DB.cur.execute(""" CREATE TABLE IF NOT EXISTS movies (
                                        mid text PRIMARY KEY,
                                        name text NOT NULL,
                                        description text NOT NULL,
                                        score integer,
                                        date timestamp
                                    ); """)

    # def select_all_movies(self):
    #     self.DB.cur.execute("SELECT * FROM movies")
    #     rows = self.DB.cur.fetchall()
    #     for row in rows:
    #         print(row)
    #
    # def delete_task(self, mid):
    #     sql = 'DELETE FROM movies WHERE mid=?'
    #     self.DB.cur.execute(sql, (mid,))
    #     self.DB.connection.commit()
    #
    # def delete_all_tasks(self):
    #     sql = 'DELETE FROM movies'
    #     self.DB.cur.execute(sql)
    #     self.DB.connection.commit()

    def add_movie(self, new_movie: Movie) -> None:
        sql = ''' INSERT INTO movies(mid,name,description,score,date)
                          VALUES(?,?,?,?,?) '''
        movie_data = (str(new_movie.mid), new_movie.name, new_movie.description, new_movie.score, new_movie.date)
        self.DB.execute(sql, movie_data)
        self.DB.commit()
        self.DB.close()

    def get_latest_movies(self, number_of_movies) -> list:
        sql = "SELECT * FROM movies ORDER BY date DESC Limit "+str(number_of_movies)
        self.DB.cur.execute(sql)
        rows = self.DB.cur.fetchall()
        if not rows:
            return None
        movies_list = []
        for row in rows:
            m = Movie(row[1], row[2], row[3], row[4], row[0])  # datetime.strptime(row[4], "%Y-%m-%d %H:%M:%S.%f%z")
            movies_list.append(m)
        return movies_list

    # def get_movie_id(self, movie_id: int) -> Movie:
    #     return next((x for x in self.movies_list if x.mid == movie_id), None)