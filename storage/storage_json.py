import json
from .istorage import IStorage


class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def _load_movies(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def _save_movies(self, movies):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            json.dump(movies, file, indent=4, ensure_ascii=False)

    def list_movies(self):
        return self._load_movies()

    def add_movie(self, title, year, rating, poster):
        movies = self._load_movies()
        movies[title] = {"year": year, "rating": rating, "poster": poster}
        self._save_movies(movies)

    def delete_movie(self, title):
        movies = self._load_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        movies = self._load_movies()
        if title in movies:
            movies[title]["rating"] = rating
            self._save_movies(movies)
