import requests

class MovieApp:
    """
    A class to represent the MovieApp.

    This class provides methods to interact with a movie storage system and
    integrates with the OMDb API to fetch movie details such as title, year,
    rating, and poster.
    """

    def __init__(self, storage):
        """
        Initializes the MovieApp instance.

        Args:
            storage (Storage): The storage system to be used for storing and
                                managing movie data.
        """
        self.storage = storage
        self.api_key = "f2dca233"

    def list_movies(self):
        """
        List all movies in the storage.

        Retrieves the list of movies stored in the storage system.

        Returns:
            list: A list of movie objects or data from the storage.
        """
        return self.storage.list_movies()

    def add_movie(self, title):
        """
        Add a movie to the storage by fetching details from the OMDb API.

        This method sends a request to the OMDb API to search for the movie by
        its title and retrieve its details (title, year, imdbRating, poster).
        If the movie is found, it adds the movie to the storage.

        Args:
            title (str): The title of the movie to be added.

        Returns:
            str: A message indicating whether the movie was successfully added
                 or if there was an error.
        """
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
        """
        Delete a movie from the storage.

        This method deletes a movie from the storage system based on its title.

        Args:
            title (str): The title of the movie to be deleted.
        """
        self.storage.delete_movie(title)

    def update_movie(self, title, rating):
        """
        Update the rating of a movie in the storage.

        This method updates the rating of an existing movie in the storage
        system.

        Args:
            title (str): The title of the movie to be updated.
            rating (str): The new rating to set for the movie.
        """
        self.storage.update_movie(title, rating)
