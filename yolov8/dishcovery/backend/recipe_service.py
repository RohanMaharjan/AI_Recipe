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

'''def get_recipes(ingredients):
    params = {
        "ingredients": ",".join(ingredients),
        "number": 5,
        "ranking": 1,
        "ignorePantry": True,
        "apiKey": settings.SPOONACULAR_API_KEY
    }

    response = requests.get(SPOONACULAR_URL, params=params)
    response.raise_for_status()

    raw_recipes = response.json()

    # 🔹 Filter response (BEST PRACTICE)
    filtered_recipes = []
    for r in raw_recipes:
        filtered_recipes.append({
            "id": r["id"],
            "title": r["title"],
            "image": r["image"],
            "usedIngredientCount": r["usedIngredientCount"],
            "missedIngredientCount": r["missedIngredientCount"],
        })

    return filtered_recipes
'''