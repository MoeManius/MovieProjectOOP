import csv
from istorage import IStorage


class StorageCsv(IStorage):
    """
    A class to represent movie storage using a CSV file.

    This class implements the IStorage interface and uses a CSV file as the
    backend to store movie data. It supports operations to list, add, delete
    movies, and save movie data back to the CSV file.
    """

    def __init__(self, file_path):
        """
        Initializes the StorageCsv instance.

        Args:
            file_path (str): The path to the CSV file where movie data will be stored.
        """
        self.file_path = file_path

    def list_movies(self):
        """
        List all movies stored in the CSV file.

        This method reads the CSV file and returns a dictionary of movies. Each
        movie is stored by its title, and the dictionary contains the movie's
        year, rating, and poster URL.

        Returns:
            dict: A dictionary where the key is the movie title and the value is
                  a dictionary containing the year, rating, and poster of the movie.
        """
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
            pass  # If the file doesn't exist, return an empty dictionary
        return movies

    def add_movie(self, title, year, rating, poster):
        """
        Add a new movie to the CSV file.

        This method appends a new movie with the given title, year, rating, and
        poster to the CSV file.

        Args:
            title (str): The title of the movie.
            year (str): The release year of the movie.
            rating (str): The IMDb rating of the movie.
            poster (str): The URL of the movie's poster image.
        """
        movies = self.list_movies()
        movies[title] = {
            "year": year,
            "rating": rating,
            "poster": poster
        }
        self._save_movies(movies)

    def delete_movie(self, title):
        """
        Delete a movie from the CSV file.

        This method removes a movie from the CSV file based on the provided title.

        Args:
            title (str): The title of the movie to be deleted.
        """
        movies = self.list_movies()
        if title in movies:
            del movies[title]
            self._save_movies(movies)

    def _save_movies(self, movies):
        """
        Save the movie data back to the CSV file.

        This method writes the updated list of movies to the CSV file.

        Args:
            movies (dict): A dictionary of movies where the key is the title
                           and the value is a dictionary containing the year,
                           rating, and poster.
        """
        # Ensure that we're writing in text mode ('w') which returns a TextIO object
        with open(self.file_path, 'w', newline='', encoding='utf-8') as file:
            fieldnames = ['title', 'year', 'rating', 'poster']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()  # Write the header row
            for title, details in movies.items():
                writer.writerow({
                    'title': title,
                    'year': details['year'],
                    'rating': details['rating'],
                    'poster': details['poster']
                })
