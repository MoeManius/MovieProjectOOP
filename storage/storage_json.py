import json
from .istorage import IStorage


class StorageJson(IStorage):
    """
    A class to represent movie storage using a JSON file.

    This class implements the IStorage interface and uses a JSON file as the
    backend to store movie data. It supports operations to list, add, delete,
    and update movies stored in the JSON file.
    """

    def __init__(self, file_path):
        """
        Initializes the StorageJson instance.

        Args:
            file_path (str): The path to the JSON file where movie data will be stored.
        """
        self.file_path = file_path

    def _load_movies(self):
        """
        Load movie data from the JSON file.

        This method reads the JSON file and returns the stored movie data. If the
        file does not exist or contains invalid data, it returns an empty dictionary.

        Returns:
            dict: A dictionary of movies, where each key is a movie title and the
                  value is a dictionary with the movie's year, rating, and poster.
        """
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}  # Return an empty dictionary if the file is not found or is invalid

    def _save_movies(self, movies):
        """
        Save movie data to the JSON file.

        This method writes the provided dictionary of movies to the JSON file, formatting
        the data with indentation for readability.

        Args:
            movies (dict): A dictionary of movies where the key is the title and the value
                           is a dictionary containing the year, rating, and poster.
        """
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(movies, file, indent=4, ensure_ascii=False)

    def list_movies(self):
        """
        List all movies stored in the JSON file.

        This method retrieves the list of movies from the JSON file and returns it
        as a dictionary.

        Returns:
            dict: A dictionary of movies, where the key is the title and the value
                  is a dictionary with the movie's details (year, rating, poster).
        """
        return self._load_movies()

    def add_movie(self, title, year, rating, poster):
        """
        Add a new movie to the JSON file.

        This method appends a new movie with the given title, year, rating, and
        poster to the JSON file.

        Args:
            title (str): The title of the movie.
            year (str): The release year of the movie.
            rating (str): The IMDb rating of the movie.
            poster (str): The URL of the movie's poster image.
        """
        movies = self._load_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        """
        Delete a movie from the JSON file.

        This method removes a movie from the JSON file based on the provided title.

        Args:
            title (str): The title of the movie to be deleted.
        """
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        """
        Update the rating of a movie in the JSON file.

        This method updates the rating of a movie identified by the title.

        Args:
            title (str): The title of the movie to be updated.
            rating (str): The new IMDb rating for the movie.
        """
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)
