import requests

class OmdbApi:
    def __init__(self):
        self.api_key = 'c4b70cf6'

    def fetch_movie_data(self, title):
        url = f"http://www.omdbapi.com/?t={title}&apikey={self.api_key}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            if data['Response'] == 'True':
                return {
                    'Title': data['Title'],
                    'Year': data['Year'],
                    'imdbRating': data['imdbRating'],
                    'Poster': data['Poster']
                }
        return None
