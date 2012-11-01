import model
import csv
import time 
from datetime import date, datetime, time


def load_users(session):
    # use u.user
    with open ('seed_data/u.user', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        session = model.connect()
        for row in reader: 
            row = row.pop().split("|")
            user = model.User (None, None, row[1], row[4])
            user.id = row[0]
            session.add(user)
        session.commit()
        

def load_movies(session):
    # use u.item
    with open ('seed_data/u.item', 'rb') as csvfile: 
        session = model.connect()
        reader = csv.reader(csvfile, delimiter = '|')

        for row in reader:
            print row
            title = row[1]
            title = title.decode("latin-1") 
            if row[2]:
                row[2] = datetime.strptime(row[2], '%d-%b-%Y')
            else:
                row[2] = None

            movie = model.Movie(title, row[2], row[4]) 
            session.add(movie)
        
        session.commit()
            

def load_ratings(session):
    # use u.data
    with open ('seed_data/u.data', 'rb') as csvfile:
        reader = csv.reader(csvfile)
        session = model.connect()
        for row in reader:
            row = row.pop().split("\t")
            rating = model.Rating(row[1], row[2], row[0])
            session.add(rating)
        
        session.commit()


    pass

def main(session):
    # You'll call each of the load_* functions with the session as an argument
    pass

if __name__ == "__main__":
    s= model.connect()
    main(s)

    load_movies(s)
