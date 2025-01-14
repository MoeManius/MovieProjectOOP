from storage_json import StorageJson
from movie_app import MovieApp


def main():
    # Create the StorageJson instance (you can provide a file path here)
    storage = StorageJson('movies.json')

    # Create the MovieApp instance with the storage
    app = MovieApp(storage)

    # Run the MovieApp
    app.run()


if __name__ == "__main__":
    main()
