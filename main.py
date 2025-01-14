from flask import Flask, render_template, request
from storage.storage_json import StorageJson
from movie_app import MovieApp

app = Flask(__name__)
storage = StorageJson('movies.json')
app_controller = MovieApp(storage)


@app.route("/")
def index():
    movies = app_controller.list_movies()
    return render_template("index_template.html", movies=movies)


@app.route("/add", methods=["POST"])
def add_movie():
    title = request.form.get("title")
    if not title:
        movies = app_controller.list_movies()
        return render_template("index_template.html", movies=movies, error="Please provide a movie title.")

    result = app_controller.add_movie(title)
    movies = app_controller.list_movies()
    return render_template("index_template.html", movies=movies, success=result)


@app.route("/delete/<string:title>", methods=["POST"])
def delete_movie(title):
    app_controller.delete_movie(title)
    movies = app_controller.list_movies()
    return render_template("index_template.html", movies=movies, success=f"{title} was deleted.")


@app.route("/update/<string:title>", methods=["POST"])
def update_movie(title):
    rating = request.form.get("rating")
    if rating:
        app_controller.update_movie(title, rating)
        movies = app_controller.list_movies()
        return render_template("index_template.html", movies=movies,
                               success=f"{title} was updated with new rating {rating}.")
    return render_template("index_template.html", movies=app_controller.list_movies(), error="Rating is required.")


if __name__ == "__main__":
    app.run(debug=True)
