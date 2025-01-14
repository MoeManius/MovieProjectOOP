from istorage import IStorage
import json

class StorageJson(IStorage):
    def __init__(self, file_path):
        """Initialize with the path to the JSON file."""
        self.file_path = file_path

    def _load_movies(self):
        """Load movies from the JSON file."""
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}  # Return an empty dictionary if the file doesn't exist
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return {}  # Return an empty dictionary if there's a decoding error

    def _save_movies(self, movies):
        """Save the movies dictionary to the JSON file."""
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(movies, file, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving movies: {e}")

    def list_movies(self):
        """Returns a dictionary of movies from the JSON file."""
        return self._load_movies()

    def add_movie(self, title, year, rating, poster):
        """Adds a new movie to the storage (JSON file)."""
        movies = self._load_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        """Deletes a movie from the storage (JSON file)."""
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)
        else:
            print(f"Movie '{title}' not found.")

    def update_movie(self, title, rating):
        """Updates the rating of an existing movie in the storage (JSON file)."""
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)
        else:
            print(f"Movie '{title}' not found.")

