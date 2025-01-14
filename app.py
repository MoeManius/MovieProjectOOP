from flask import Flask, render_template
from storage.storage_json import StorageJson

app = Flask(__name__)

# Initialize storage (choose the storage backend, like JSON for now)
storage = StorageJson("movies.json")


@app.route('/')
def index():
    # Get the list of movies from storage
    movies = storage.list_movies()

    # Generate the movie grid HTML content
    movie_grid_html = ""
    for title, movie in movies.items():
        movie_grid_html += f'''
        <li>
            <div class="movie">
                <img src="{movie['poster']}" alt="{movie['title']}" class="movie-poster"/>
                <div class="movie-title">{movie['title']}</div>
                <div class="movie-year">{movie['year']}</div>
            </div>
        </li>
        '''

    # Render the HTML template with the movie grid and title
    return render_template('index_template.html',
                           title="My Movie App",
                           movie_grid=movie_grid_html)


if __name__ == "__main__":
    app.run(debug=True)
