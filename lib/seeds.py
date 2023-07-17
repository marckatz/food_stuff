#!/usr/bin/env python3
from foodstuff import Base, session
from models import *

if __name__ == '__main__':

    #delete existing tables
    session.query(Recipe).delete()
    session.query(RecipeIngredient).delete()
    session.query(Ingredient).delete()

    ingredient_names = ['water', 'milk', 'eggs', 'sugar', 'oil', 'butter', 'flour', 'baking soda', 'tomato', 'bread', 'lettuce', 'mayo']
    for i in ingredient_names:
        session.add(Ingredient(name=i))
    session.commit()

    cookie_recipe = Recipe(directions='just cook it lol')
    blt_recipe = Recipe(directions='put it all together')

    session.add_all([cookie_recipe, blt_recipe])
    session.commit()

    session.close()