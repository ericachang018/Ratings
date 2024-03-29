from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import sessionmaker

ENGINE = None
Session = None

Base = declarative_base()

### Class declarations go here
class User(Base):
	__tablename__ = "users"

	id = Column(Integer, primary_key = True)
	email = Column(String(64), nullable = True)
	password = Column(String(64), nullable = True)
	age = Column(Integer, nullable = True)
	zipcode = Column(String(15), nullable = True)

	def __init__(self, email = None, password = None, age = None, zipcode = None):
		self.email = email 
		self.password = password
		self.age = age
		self.zipcode = zipcode 


class Movie(Base):
	__tablename__ = "movies"
	id = Column(Integer, primary_key = True)
	name = Column(String(64), nullable = False)
	released_at = Column(DateTime, nullable = True)
	imdb_url = Column(String(64), nullable = True)

	def __init__(self, name = None, released_at = None, imdb_url= None):
		self.name = name 
		self.released_at = released_at
		self.imdb_url= imdb_url
		
class Rating(Base): 
	__tablename__ = "ratings"
	id = Column(Integer, primary_key = True)
	user_id = Column(Integer, ForeignKey('users.id'))
	movie_id = Column(Integer)
	rating  = Column(Integer, nullable = True)

	user = relationship("User", 
			backref=backref("ratings", order_by=id))

	def __init__(self, movie_id = None, rating = None, user_id = None):
		self.movie_id = movie_id
		self.rating = rating
		self.user_id = user_id


### End class declarations
def connect():
	global ENGINE
	global Session

	ENGINE = create_engine("sqlite:///ratings.db", echo=False)
	Session = sessionmaker(bind=ENGINE)
	return Session()


def main():
    """In case we need this for something"""
    pass

if __name__ == "__main__":
    main()
