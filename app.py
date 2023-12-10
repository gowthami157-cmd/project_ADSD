# project_ADSD
from bottle import route, post, run, template, redirect, request
import database

# Initialize the database
database.initialize_database()

@route("/")
def get_index():
    redirect("/movies")

@route("/movies")
def get_movies():
    movies = database.get_all_movies()
    return template("movies.tpl", movies=movies)

@route("/movies/add")
def get_add_movie():
    return template("add_movie.tpl")

@post("/movies/add")
def post_add_movie():
    title = request.forms.get("title")
    genre = request.forms.get("genre")
    database.add_movie(title, genre)
    redirect("/movies")

@route("/movies/<movie_id>")
def get_movie_details(movie_id):
    movie = database.get_movie_details(movie_id)
    ratings = database.get_ratings_for_movie(movie_id)
    return template("movie_details.tpl", movie=movie, ratings=ratings)

@route("/movies/<movie_id>/add_rating")
def get_add_rating(movie_id):
    return template("add_rating.tpl", movie_id=movie_id)

@post("/movies/<movie_id>/add_rating")
def post_add_rating(movie_id):
    rating_value = request.forms.get("rating")
    database.add_rating(movie_id, rating_value)
    redirect(f"/movies/{movie_id}")

@route("/movies/<movie_id>/update")
def get_update_movie(movie_id):
    movie = database.get_movie_details(movie_id)
    return template("update_movie.tpl", movie=movie)

@post("/movies/<movie_id>/update")
def post_update_movie(movie_id):
    title = request.forms.get("title")
    genre = request.forms.get("genre")
    database.update_movie(movie_id, title, genre)
    redirect("/movies")

@route("/movies/<movie_id>/delete")
def get_delete_movie(movie_id):
    database.delete_movie(movie_id)
    redirect("/movies")

run(host='localhost', port=8080)
