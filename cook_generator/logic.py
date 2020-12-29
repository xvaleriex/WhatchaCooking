from cook_generator.models import Meal
import random


def pick_random_recipe() -> int:
    """
    Picks random recipe number and return its value to be used to access a recipe via url
    :return: int recipe number (primary key in a database)
    """
    all_recipes = Meal.objects.all()
    recipes_counter = all_recipes.len()
    generared_recipe_num = random.randint(1, recipes_counter)
    return generared_recipe_num
