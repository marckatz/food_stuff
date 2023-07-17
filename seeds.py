#!/usr/bin/env python3
from lib.foodstuff import session
from lib.models import *

if __name__ == '__main__':
    # engine = create_engine('sqlite:///../food_stuff.db')
    # Session = sessionmaker(bind=engine)
    # session = Session()

    #delete existing tables
    session.query(Recipe).delete()
    session.query(RecipeIngredient).delete()
    session.query(Ingredient).delete()

    ingredient_names = ['water', 'milk', 'eggs', 'sugar', 'oil', 'butter', 
                        'flour', 'chocolate chips', 'baking soda', 'tomato', 
                        'bread', 'lettuce', 'mayo']
    for i in ingredient_names:
        session.add(Ingredient(name=i))
    session.commit()

    cookie_recipe = Recipe(name='Cookie',directions='just cook it lol')
    blt_recipe = Recipe(name='BLT',directions='put it all together')

    session.add_all([cookie_recipe, blt_recipe])
    session.commit()

    cookie_ingredient_ids = [1,2,3,4,6,7,8,9]
    blt_ingredient_ids = [10,11,12,13]
    for i in cookie_ingredient_ids:
        session.add(RecipeIngredient(
            ingredient_id = i,
            recipe_id = 1
        ))
    for i in blt_ingredient_ids:
        session.add(RecipeIngredient(
            ingredient_id = i,
            recipe_id = 2
        ))
    session.commit()

    session.close()