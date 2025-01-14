import requests

API_KEY = "f2dca233"
OMDB_API_URL = "http://www.omdbapi.com/"


def fetch_movie_data(title):
    """
    Fetch movie data from the OMDB API using the movie title.
    """
    try:
        response = requests.get(OMDB_API_URL, params={"apikey": API_KEY, "t": title})
        response.raise_for_status()
        data = response.json()

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
        return None
