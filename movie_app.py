from istorage import IStorage
from omdb_api import OmdbApi


class MovieApp:
    def __init__(self, storage: IStorage):
        self._storage = storage

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        for movie, details in movies.items():
            print(f"{movie} (Year: {details['year']}): {details['rating']}")

    def _command_add_movie(self):
        title = input("Enter movie title: ").strip()
        omdb = OmdbApi()
        movie_data = omdb.fetch_movie_data(title)

        if movie_data:
            self._storage.add_movie(movie_data['Title'], movie_data['Year'], movie_data['imdbRating'],
                                    movie_data['Poster'])
            print("Movie added successfully.")
        else:
            print("Movie not found or error fetching data.")

    def _command_movie_stats(self):
        movies = self._storage.list_movies()
        print(f"Total movies: {len(movies)}")

    def _generate_website(self):
        pass

    def run(self):
        while True:
            print("Movie App Menu")
            print("1. List movies")
            print("2. Add movie")
            print("3. Movie stats")
            print("4. Exit")
            choice = input("Enter choice: ").strip()
            if choice == '1':
                self._command_list_movies()
            elif choice == '2':
                self._command_add_movie()
            elif choice == '3':
                self._command_movie_stats()
            elif choice == '4':
                break
            else:
                print("Invalid choice. Try again.")
