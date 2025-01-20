import requests

API_KEY = "f2dca233"
OMDB_API_URL = "http://www.omdbapi.com/"


def fetch_movie_data(title):
    """
    Fetch movie data from the OMDb API using the movie title.

    This function sends a request to the OMDb API to retrieve movie details based
    on the provided title. If the movie is found, it returns a dictionary with
    the movie's title, year, IMDb rating, and poster URL. If there is an error
    or the movie is not found, it returns None.

    Args:
        title (str): The title of the movie to fetch data for.

    Returns:
        dict or None: A dictionary containing the movie's title, year, IMDb rating,
                      and poster if found, otherwise None.
    """
    try:
        # Send a GET request to the OMDb API
        response = requests.get(OMDB_API_URL, params={"apikey": API_KEY, "t": title})
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()

        # Check if the response is valid
        if data.get("Response") == "True":
            return {
                "title": data.get("Title"),
                "year": data.get("Year"),
                "rating": data.get("imdbRating"),
                "poster": data.get("Poster")
            }
        else:
            return None
    except requests.RequestException:
        # Return None if there's an error in the request
        return None
