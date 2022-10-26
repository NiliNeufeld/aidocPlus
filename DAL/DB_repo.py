from DAL.movies_repo import MoviesRepo
from common.movie import Movie
from common.movie_summary import MovieSummary
from DAL.DB_handler import DBHandler
from typing import List


class DBRepo(MoviesRepo):

    def __init__(self, db_handler: DBHandler):
        self.DB = db_handler

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


    def add_movie(self, new_movie: Movie) -> None:
        sql = ''' INSERT INTO movies(mid,name,description,score,date)
                          VALUES(?,?,?,?,?) '''
        movie_data = (str(new_movie.mid), new_movie.name, new_movie.description, new_movie.score, new_movie.date)
        self.DB.execute(sql, movie_data)
        self.DB.commit()
        self.DB.close()

    def get_latest_movies(self, number_of_movies: int) -> List[MovieSummary]:
        sql = "SELECT * FROM movies ORDER BY date DESC Limit "+str(number_of_movies)
        self.DB.cur.execute(sql)
        rows = self.DB.cur.fetchall()
        if not rows:
            return None
        movies_list = []
        for row in rows:
            m = MovieSummary(row[1], row[0])
            movies_list.append(m)
        return movies_list

    def get_movie_id(self, movie_id: str) -> Movie:
        sql = "SELECT * FROM movies WHERE mid ="+"\'"+movie_id+"\'"
        self.DB.cur.execute(sql)
        rows = self.DB.cur.fetchall()
        if not rows:
            return None
        for row in rows:
            m = Movie(row[1], row[2], row[3], row[4], row[0])
        return m

    def search_movies(self, value) -> List[MovieSummary]:
        sql = "SELECT * FROM movies WHERE name LIKE "+"\'%"+value+"%\'"
        self.DB.cur.execute(sql)
        rows = self.DB.cur.fetchall()
        if not rows:
            return None
        movies_list = []
        for row in rows:
            m = MovieSummary(row[1], row[0])
            movies_list.append(m)
        return movies_list
