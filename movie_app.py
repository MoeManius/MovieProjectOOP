from omdb_api import OmdbApi


class MovieApp:
    def __init__(self, storage, omdb_api):
        self._storage = storage
        self._omdb_api = omdb_api

    def _command_add_movie(self):
        """Handle adding a movie by fetching data from OMDB API."""
        title = input("Enter movie title: ")
        movie_data = self._omdb_api.get_movie_data(title)

        if movie_data:
            print(f"Adding movie: {movie_data['title']}, Year: {movie_data['year']}, Rating: {movie_data['rating']}")
            self._storage.add_movie(movie_data['title'], movie_data['year'], movie_data['rating'], movie_data['poster'])
            print("Movie added successfully.")
        else:
            print("Failed to fetch movie data from OMDB.")

    def _command_list_movies(self):
        movies = self._storage.list_movies()
        if movies:
            for title, data in movies.items():
                print(f"Title: {title}, Year: {data['year']}, Rating: {data['rating']}")
        else:
            print("No movies found.")

    def _command_movie_stats(self):
        movies = self._storage.list_movies()
        if movies:
            total_movies = len(movies)
            avg_rating = sum([movie['rating'] for movie in movies.values()]) / total_movies if total_movies > 0 else 0
            print(f"Total movies: {total_movies}, Average rating: {avg_rating}")
        else:
            print("No movies found.")

    def _generate_website(self):
        # Logic for generating website would go here (similar to your previous code)
        pass

    def run(self):
        while True:
            print("\nMovie App Menu:")
            print("1. List Movies")
            print("2. Add Movie")
            print("3. Movie Stats")
            print("4. Generate Website")
            print("5. Exit")

            choice = input("Enter command: ")

            if choice == '1':
                self._command_list_movies()
            elif choice == '2':
                self._command_add_movie()
            elif choice == '3':
                self._command_movie_stats()
            elif choice == '4':
                self._generate_website()
            elif choice == '5':
                break
            else:
                print("Invalid command.")
