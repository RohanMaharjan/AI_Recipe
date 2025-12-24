import requests
from django.conf import settings

SPOONACULAR_URL = "https://api.spoonacular.com/recipes/findByIngredients"

def get_recipes(ingredients):
    params = {
        "ingredients": ",".join(ingredients),
        "number": 5,
        "ranking": 1,
        "ignorePantry": True,
        "apiKey": settings.SPOONACULAR_API_KEY
    }

    response = requests.get(SPOONACULAR_URL, params=params)
    response.raise_for_status()

    return response.json()
