import requests

class OmdbApi:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://www.omdbapi.com/"

    def get_movie_data(self, title):
        """Fetch movie data from OMDB API based on the movie title."""
        params = {
            't': title,
            'apikey': self.api_key
        }
        response = requests.get(self.base_url, params=params)

        if response.status_code == 200:
            data = response.json()
            if data['Response'] == 'True':
                # Return relevant movie data (you can expand this as needed)
                return {
                    'title': data['Title'],
                    'year': int(data['Year']),
                    'rating': float(data.get('imdbRating', 0)),
                    'poster': data.get('Poster', None)
                }
            else:
                print(f"Error: {data['Error']}")
        else:
            print("Error: Failed to fetch data from OMDB.")
        return None
