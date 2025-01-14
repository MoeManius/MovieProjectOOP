from istorage import IStorage

class MovieApp:
    def __init__(self, storage: IStorage):
        """Initialize the MovieApp with a storage instance."""
        self._storage = storage

    def _command_list_movies(self):
        """List all movies in the storage."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available.")
        else:
            for title, details in movies.items():
                print(f"{title} (Year: {details['year']}): Rating {details['rating']}")

    def _command_movie_stats(self):
        """Calculate and display movie statistics."""
        movies = self._storage.list_movies()
        if not movies:
            print("No movies available to calculate statistics.")
            return

        ratings = [details['rating'] for details in movies.values()]
        average_rating = sum(ratings) / len(ratings)
        print(f"Average rating: {average_rating:.2f}")

    def _command_add_movie(self):
        """Add a new movie to the storage."""
        title = input("Enter the movie title: ").strip()
        year = input("Enter the movie year: ").strip()
        rating = float(input("Enter the movie rating: ").strip())
        poster = input("Enter the movie poster URL: ").strip()
        self._storage.add_movie(title, year, rating, poster)
        print(f"Movie '{title}' added successfully.")

    def _command_delete_movie(self):
        """Delete a movie from the storage."""
        title = input("Enter the movie title to delete: ").strip()
        self._storage.delete_movie(title)
        print(f"Movie '{title}' deleted successfully.")

    def _command_update_movie(self):
        """Update the rating of a movie."""
        title = input("Enter the movie title to update: ").strip()
        rating = float(input(f"Enter the new rating for '{title}': ").strip())
        self._storage.update_movie(title, rating)
        print(f"Rating for '{title}' updated successfully.")

    def _generate_website(self):
        """Generate a simple website (for future use)."""
        # Placeholder for generating a website (this can be expanded later)
        print("Generating website...")

    def _display_menu(self):
        """Display the menu options."""
        print("\n********** Movie App **********")
        print("1. List Movies")
        print("2. Add Movie")
        print("3. Update Movie Rating")
        print("4. Delete Movie")
        print("5. Show Movie Stats")
        print("6. Generate Website")
        print("0. Exit")

    def run(self):
        """Run the MovieApp."""
        while True:
            self._display_menu()
            choice = input("Enter your choice: ").strip()
            if choice == '0':
                print("Exiting the Movie App.")
                break
            elif choice == '1':
                self._command_list_movies()
            elif choice == '2':
                self._command_add_movie()
            elif choice == '3':
                self._command_update_movie()
            elif choice == '4':
                self._command_delete_movie()
            elif choice == '5':
                self._command_movie_stats()
            elif choice == '6':
                self._generate_website()
            else:
                print("Invalid choice, please try again.")
