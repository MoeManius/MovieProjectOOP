from flask import Flask, render_template, request
from storage.storage_json import StorageJson
from movie_app import MovieApp

app = Flask(__name__)
storage = StorageJson('movies.json')
app_controller = MovieApp(storage)


@app.route("/")
def index():
    """
    Render the index page with the list of movies.

    This function retrieves the list of movies from the app controller and
    passes it to the `index_template.html` for rendering.

    Returns:
        Response: The rendered HTML page with the list of movies.
    """
    movies = app_controller.list_movies()
    return render_template("index_template.html", movies=movies)


@app.route("/add", methods=["POST"])
def add_movie():
    """
    Add a new movie to the collection.

    This function handles the addition of a movie by accepting the movie's
    title through a POST request. If no title is provided, an error message
    is shown. After the movie is added, the updated list of movies is displayed.

    Returns:
        Response: The rendered HTML page with the updated list of movies.
    """
    title = request.form.get("title")
    if not title:
        movies = app_controller.list_movies()
        return render_template(
            "index_template.html", movies=movies, error="Please provide a movie title."
        )

    result = app_controller.add_movie(title)
    movies = app_controller.list_movies()
    return render_template("index_template.html", movies=movies, success=result)


@app.route("/delete/<string:title>", methods=["POST"])
def delete_movie(title):
    """
    Delete a movie from the collection.

    This function handles the deletion of a movie based on its title. Once the
    movie is deleted, the updated list of movies is displayed.

    Args:
        title (str): The title of the movie to be deleted.

    Returns:
        Response: The rendered HTML page with the updated list of movies.
    """
    app_controller.delete_movie(title)
    movies = app_controller.list_movies()
    return render_template("index_template.html", movies=movies, success=f"{title} was deleted.")


@app.route("/update/<string:title>", methods=["POST"])
def update_movie(title):
    """
    Update the rating of a movie.

    This function handles updating the rating of a movie based on its title.
    If a new rating is provided, the movie's rating is updated. Otherwise,
    an error message is shown. The updated list of movies is displayed after the update.

    Args:
        title (str): The title of the movie to update.

    Returns:
        Response: The rendered HTML page with the updated list of movies.
    """
    rating = request.form.get("rating")
    if rating:
        app_controller.update_movie(title, rating)
        movies = app_controller.list_movies()
        return render_template(
            "index_template.html", movies=movies, success=f"{title} was updated with new rating {rating}."
        )

    return render_template("index_template.html", movies=app_controller.list_movies(), error="Rating is required.")


if __name__ == "__main__":
    app.run(debug=True)
