import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        self.file_path = file_path

    def list_movies(self):
        movies = {}
        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row['title']
                    movies[title] = {
                        "year": row['year'],
                        "rating": row['rating'],
                        "poster": row['poster']
                    }
        except FileNotFoundError:
            pass
        return movies

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        movies[title] = {
            "year": year,
            "rating": rating,
            "poster": poster
        }
        self._save_movies(movies)

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def _save_movies(self, movies):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, details in movies.items():
                writer.writerow({
                    'title': title,
                    'year': details['year'],
                    'rating': details['rating'],
                    'poster': details['poster']
                })
