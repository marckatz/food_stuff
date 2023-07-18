#!/usr/bin/env python3
import ipdb
from lib.foodstuff import session
from lib.models import *

if __name__=='__main__':

    ingredients = session.query(Ingredient).all()
    recipes = session.query(Recipe).all()
    recipe_ingredients = session.query(RecipeIngredient).all()

    ipdb.set_trace()

    session.close()