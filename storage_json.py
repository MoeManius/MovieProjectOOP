import json
from istorage import IStorage

class StorageJson(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}
        except json.JSONDecodeError:
            return {}

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        movies[title] = {
            'year': year,
            'rating': rating,
            'poster': poster
        }
        self.save_movies(movies)

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self.save_movies(movies)

    def update_movie(self, title, rating):
        movies = self.list_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self.save_movies(movies)

    def save_movies(self, movies):
        try:
            with open(self.file_path, 'w', encoding='utf-8') as file:
                json.dump(movies, file, indent=4, ensure_ascii=False)
        except IOError as e:
            print(f"Error saving movies: {e}")
