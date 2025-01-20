# Movie Management App

This is a simple movie management app built with Python, Flask, and supports multiple storage backends (CSV and JSON) for storing movie data. The app allows users to view, add, update, and delete movies from the storage, with the ability to persist movie information in a CSV or JSON file.

## Features

- View a list of movies.
- Add new movies with title, year, rating, and poster.
- Update a movie's IMDb rating.
- Delete a movie from the list.
- Choose between different storage backends (CSV or JSON).

## Requirements

- Python 3.x
- Flask (`pip install flask`)
- Requests (`pip install requests`)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/movie-management-app.git
    cd movie-management-app
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Usage

### Running the Flask Application

1. Run the Flask app:

    ```bash
    python app.py
    ```

2. Visit the app in your browser at `http://127.0.0.1:5000/`.

### Storage Backends

This app supports two storage options:

- **JSON**: The movie data is stored in a `movies.json` file.
- **CSV**: The movie data is stored in a `movies.csv` file.

You can switch between storage backends by changing the initialization of `StorageJson` or `StorageCsv` in the app.

#### Example of switching to JSON storage:

```python
# Initialize storage with JSON backend
storage = StorageJson('movies.json')
Example of switching to CSV storage:
python
Kopieren
Bearbeiten
# Initialize storage with CSV backend
storage = StorageCsv('movies.csv')
OMDb API Integration
The app uses the OMDb API to fetch movie data based on the title. You can replace the default API key in the code with your own key by signing up at OMDb.

python
Kopieren
Bearbeiten
API_KEY = "your_api_key_here"