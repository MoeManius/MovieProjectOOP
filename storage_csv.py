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
                    movies[row['title']] = {
                        'rating': row['rating'],
                        'year': row['year'],
                        'poster': row['poster']
                    }
        except FileNotFoundError:
            return {}
        return movies

    def add_movie(self, title, year, rating, poster):
        movies = self.list_movies()
        movies[title] = {
            'year': year,
            'rating': rating,
            'poster': poster
        }
        self._save_movies(movies)

    def delete_movie(self, title):
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def update_movie(self, title, rating):
        movies = self.list_movies()
        if title in movies:
            movies[title]['rating'] = rating
            self._save_movies(movies)

    def _save_movies(self, movies):
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            writer = csv.DictWriter(file, fieldnames=['title', 'year', 'rating', 'poster'])
            writer.writeheader()
            for title, details in movies.items():
                writer.writerow({
                    'title': title,
                    'year': details['year'],
                    'rating': details['rating'],
                    'poster': details['poster']
                })
