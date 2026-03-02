import requests

API_KEY = "1T0hvkJJmSVQb7dw5XNJqdeI19zfPGtKdaObEflj"
API_URL = "https://api.api-ninjas.com/v1/animals"


def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
      'name': ...,
      'taxonomy': {...},
      'locations': [...],
      'characteristics': {...}
    }
    """
    headers = {"X-Api-Key": API_KEY}
    params = {"name": animal_name}

    response = requests.get(API_URL, headers=headers, params=params)
    return response.json()