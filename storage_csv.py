import csv
from istorage import IStorage

class StorageCsv(IStorage):
    def __init__(self, file_path):
        """Initialize with the file path."""
        self._file_path = file_path

    def _read_csv(self):
        """Read the CSV file and return the data as a dictionary."""
        movies = {}
        try:
            with open(self._file_path, mode='r', newline='', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    title = row['title']
                    movies[title] = {
                        'rating': float(row['rating']),
                        'year': int(row['year'])
                    }
        except FileNotFoundError:
            # If the file doesn't exist, return an empty dictionary
            pass
        return movies

    def _write_csv(self, movies):
        """Write the movies dictionary to a CSV file."""
        with open(self._file_path, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['title', 'rating', 'year']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for title, details in movies.items():
                writer.writerow({
                    'title': title,
                    'rating': details['rating'],
                    'year': details['year']
                })

    def list_movies(self):
        """List movies from the CSV file."""
        return self._read_csv()

    def add_movie(self, title, year, rating, poster=None):
        """Add a movie to the CSV file."""
        movies = self._read_csv()
        if title not in movies:
            movies[title] = {'rating': rating, 'year': year}
            self._write_csv(movies)

    def delete_movie(self, title):
        """Delete a movie from the CSV file."""
        movies = self._read_csv()
        if title in movies:
            del movies[title]
            self._write_csv(movies)

    def update_movie(self, title, rating):
        """Update a movie's rating in the CSV file."""
        movies = self._read_csv()
        if title in movies:
            movies[title]['rating'] = rating
            self._write_csv(movies)
