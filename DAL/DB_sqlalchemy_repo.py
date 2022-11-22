from DAL.movies_repo import MoviesRepo
from common.movie import Movie
from common.movie_summary import MovieSummary
from sqlite3 import Error
from typing import List

from sqlalchemy import create_engine, Column, String, Integer, DateTime, delete
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

Base = declarative_base()


class DBMovie(Base):

    __tablename__ = "movies"

    mid = Column(String, primary_key=True)
    name = Column(String)
    description = Column(String)
    score = Column(Integer)
    date = Column(String) # TODO - read handeling datetime

    def __init__(self, mid, name, description, score, date):
        self.mid = mid
        self.name = name
        self.description = description
        self.score = score
        self.date = date

    def __repr__(self):
        return "<movie(mid='%s', name='%s',description='%s', score='%s', date='%s')>" % (
            self.mid,
            self.name,
            self.description,
            self.score,
            self.date,
        )


class DBSQLAlchemyMovieRepo(MoviesRepo):

    def __init__(self):
        self.engine = create_engine('sqlite:///aidocPlusAlchemy.db', echo=True)
        Session = scoped_session(sessionmaker(bind=self.engine))
        self.session = Session()
        self.Base = Base
        self.Base.metadata.create_all(self.engine)
        # self.db_location = db_location

    def add_movie(self, new_movie: Movie) -> None:
        movie = DBMovie(str(new_movie.mid), new_movie.name, new_movie.description, new_movie.score, new_movie.date)
        self.session.add(movie)
        self.session.commit()
        self.session.close()

    def get_latest_movies(self, number_of_movies: int) -> List[MovieSummary]:
        latest = self.session.query(DBMovie).order_by(DBMovie.date)[0:number_of_movies]
        movies_list = []
        if not latest:
            return None
        for movie in latest:
            m = MovieSummary(mid=movie.mid, name=movie.name)
            movies_list.append(m)
        self.session.close()
        return movies_list

    def get_movie_id(self, movie_id: str) -> Movie:
        print("get movie id")
        results = self.session.query(DBMovie).filter(DBMovie.mid == movie_id).first()
        if results is None:
            return None
        movie = Movie(results.name, results.description, results.score, results.date, results.mid)
        self.session.close()
        return movie

    def search_movies(self, value) -> List[MovieSummary]:
        print("searching movie")
        matched_movies = self.session.query(DBMovie).filter(DBMovie.name.like("%" + value + "%")).all()
    # query.filter(User.name.like('%ed%'))
        if not matched_movies:
            return None
        movies_list = []
        for movie in matched_movies:
            m = MovieSummary(mid=movie.mid, name=movie.name)
            movies_list.append(m)
        self.session.close()
        return movies_list

    def delete_movie(self, movie_id) -> bool:
        print("delete movie")
        if self.get_movie_id(movie_id) is None:
            return False
        self.session.query(DBMovie).filter(DBMovie.mid == movie_id).delete()
        self.session.commit()
        self.session.close()
        return True

    def delete_all_movies(self) -> bool:
        print("delete all movie")
        try:
            self.session.query(DBMovie).delete()
        except Error:
            return False
        else:
            return True
        finally:
            self.session.close()



