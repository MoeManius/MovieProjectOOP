from storage_json import StorageJson
from omdb_api import OmdbApi
from movie_app import MovieApp

def main():
    # Initialize storage and OMDB API
    storage = StorageJson('movies.json')
    omdb_api = OmdbApi('c4b70cf6')  # Your OMDB API key

    # Create the MovieApp instance with storage and OMDB API
    app = MovieApp(storage, omdb_api)

    # Run the app
    app.run()

if __name__ == '__main__':
    main()
