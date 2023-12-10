# project_ADSD
import sqlite3

connection = sqlite3.connect("movie_rating_system.db")

def initialize_database():
    cursor = connection.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS Movies")
        cursor.execute("DROP TABLE IF EXISTS Ratings")
    except:
        pass

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Movies (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            genre TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Ratings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            movie_id INTEGER,
            rating INTEGER,
            FOREIGN KEY (movie_id) REFERENCES Movies (id)
        )
    ''')

    for movie in [
        {'title': 'Avengers', 'genre': 'Action'},
        {'title': 'RRR', 'genre': 'Drama'},
        {'title': 'Animal', 'genre': 'Action'},
    ]:
        cursor.execute(f"INSERT INTO Movies (title, genre) VALUES ('{movie['title']}', '{movie['genre']}')")

    for rating in [
        {'movie_id': 1, 'rating': 5},
        {'movie_id': 2, 'rating': 4},
        {'movie_id': 3, 'rating': 5},
    ]:
        cursor.execute(f"INSERT INTO Ratings (movie_id, rating) VALUES ({rating['movie_id']}, {rating['rating']})")

    connection.commit()

def get_all_movies():
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM Movies")
    columns = [column[0] for column in cursor.description]
    movies = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return movies

def add_movie(title, genre):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Movies (title, genre) VALUES ('{title}', '{genre}')")
    connection.commit()

def get_movie_details(movie_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM Movies WHERE id = {movie_id}")
    columns = [column[0] for column in cursor.description]
    movie = dict(zip(columns, cursor.fetchone()))
    return movie

def get_ratings_for_movie(movie_id):
    cursor = connection.cursor()
    cursor.execute(f"SELECT  rating FROM Ratings WHERE movie_id = {movie_id}")
    ratings = cursor.fetchall()
    return ratings

def add_rating(movie_id, rating):
    cursor = connection.cursor()
    cursor.execute(f"INSERT INTO Ratings (movie_id, rating) VALUES ({movie_id}, {rating})")
    connection.commit()

def update_movie(movie_id, title, genre):
    cursor = connection.cursor()
    cursor.execute(f"UPDATE Movies SET title = '{title}', genre = '{genre}' WHERE id = {movie_id}")
    connection.commit()

def delete_movie(movie_id):
    cursor = connection.cursor()
    cursor.execute(f"DELETE FROM Movies WHERE id = {movie_id}")
    connection.commit()

if __name__ == "__main__":
    initialize_database()
