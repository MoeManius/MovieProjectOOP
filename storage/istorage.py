from abc import ABC, abstractmethod


class IStorage(ABC):
    """
    An abstract base class for movie storage.

    This class defines the common interface that all storage backends must implement.
    It provides abstract methods for listing, adding, deleting, and updating movies.
    Any class that wants to serve as a storage backend for the movie app should inherit
    from this class and implement the abstract methods.
    """

    @abstractmethod
    def list_movies(self):
        """
        List all movies in the storage.

        This method should retrieve and return all the stored movies.

        Returns:
            dict: A dictionary of movies, where the key is the movie title and
                  the value is a dictionary with the movie's details (e.g., year, rating, poster).
        """
        pass

    @abstractmethod
    def add_movie(self, title, year, rating, poster):
        """
        Add a movie to the storage.

        This method should add a new movie to the storage with the provided details.

        Args:
            title (str): The title of the movie.
            year (str): The release year of the movie.
            rating (str): The IMDb rating of the movie.
            poster (str): The URL of the movie's poster image.
        """
        pass

    @abstractmethod
    def delete_movie(self, title):
        """
        Delete a movie from the storage.

        This method should remove a movie from the storage based on the provided title.

        Args:
            title (str): The title of the movie to be deleted.
        """
        pass

    @abstractmethod
    def update_movie(self, title, rating):
        """
        Update the rating of an existing movie in the storage.

        This method should update the rating of a movie identified by the title.

        Args:
            title (str): The title of the movie to be updated.
            rating (str): The new IMDb rating for the movie.
        """
        pass
