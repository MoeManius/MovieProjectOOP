import requests

class MovieApp:
    def __init__(self, storage):
        self.storage = storage
        self.api_key = "f2dca233"

    def list_movies(self):
        return self.storage.list_movies()

    def add_movie(self, title):
        # Call the OMDb API to search for the movie
        url = f"http://www.omdbapi.com/?t={title}&apikey={self.api_key}"
        response = requests.get(url)
        movie_data = response.json()

        # Debugging the API response
        print(f"OMDb API response: {movie_data}")  # Log the response to console

        if movie_data.get("Response") == "True":
            # Extract movie details
            title = movie_data.get("Title")
            year = movie_data.get("Year")
            rating = movie_data.get("imdbRating")
            poster = movie_data.get("Poster")

            # Add the movie to the storage
            self.storage.add_movie(title, year, rating, poster)
            return f"{title} has been added successfully!"
        else:
            # Log any errors from the API response
            error_message = movie_data.get("Error", "Movie not found.")
            print(f"Error from OMDb API: {error_message}")  # Log error response to console
            return f"Error: {error_message}"

    def delete_movie(self, title):
        self.storage.delete_movie(title)

    def update_movie(self, title, rating):
        self.storage.update_movie(title, rating)
