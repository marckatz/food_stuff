#!/usr/bin/env python3
from lib.foodstuff import session
from lib.models import *

if __name__ == '__main__':

    #delete existing tables
    session.query(Recipe).delete()
    session.query(RecipeIngredient).delete()
    session.query(Ingredient).delete()
    session.query(FridgeIngredient).delete()
    session.query(Fridge).delete()

    ingredient_names = ['water', 'milk', 'eggs', 'sugar', 'oil', 'butter', 
                        'flour', 'chocolate chips', 'baking soda', 'tomato', 
                        'bread', 'lettuce', 'mayo', 'bacon', 'vanilla', 'active dry yeast', 'olive oil', 'salt', 'semolina flour', 'canned tomatoes', 'mozzarella cheese']
    for i in ingredient_names:
        session.add(Ingredient(name=i))
    session.commit()

    cookie_recipe = Recipe(name='Chocolate Chip Cookies',directions='Directions: \n 1: Preheat oven to 375 degrees and line baking sheet with parchment paper. \n 2: In a separate bowl mix 3 cups flour, 1 tsp baking soda, 1 tsp salt, 1/2 tsp baking powder. Set aside.\n 3: Cream together 1 cup salted & softened butter and 1 cup white sugar and 1 cup light brown sugar packed until combined.\n 4: Beat in 2 eggs and 2 tsp vanilla until fluffy. \n 5: Mix in the dry ingredients until combined. \n 6: Add 12 oz package of chocolate chips and mix well. \n 7: Roll 2-3 TBS (depending on how large you like your cookies) of dough at a time into balls and place them evenly spaced on your prepared cookie sheets. \n 8: Bake in preheated oven for approximately 8-10 minutes. Take them out when they are just BARELY starting to turn brown. \n 9: Let them sit on the baking pan for 2 minutes before removing to cooling rack.\n 10: Enjoy!')
    blt_recipe = Recipe(name='BLT',directions='Directions: \n 1: Put it all together.')
    pizza_recipe = Recipe(name='Pizza', directions='Directions: \n 1: “Bloom” the yeast by sprinkling 1 tsp sugar and 2 tsps yeast in the warm water. Let sit for 10 minutes, until bubbles form on the surface. \n 2: In a large bowl, combine 7 cups of flour and 1 1/2 tsps salt. Make a well in the middle and add the 6 tbsps olive oil and bloomed yeast mixture. Using a spoon, mix until a shaggy dough begins to form. \n 3: Once the flour is mostly hydrated, turn the dough out onto a clean work surface and knead for 10-15 minutes. The dough should be soft, smooth, and bouncy. Form the dough into a taut round. \n 4: Grease a clean, large bowl with olive oil and place the dough inside, turning to coat with the oil. Cover with plastic wrap. Let rise for at least an hour, or up to 24 hours.\n 5: Punch down the dough and turn it out onto a lightly floured work surface. Knead for another minute or so, then cut into 4 equal portions and shape into rounds.\n 6: Lightly flour the dough, then cover with a kitchen towel and let rest for another 30 minutes to an hour while you prepare the sauce and any other ingredients.\n 7: Preheat the oven as high as your oven will allow, between 450-500˚F (230-260˚C). Place a pizza stone, heavy baking sheet (turn upside down so the surface is flat), or cast iron skillet in the oven. \n 8: Meanwhile, make the tomato sauce: Add 1 tbsp salt to the 28 oz can of tomatoes and puree. \n 9: Once the dough has rested, take a portion and start by poking the surface with your fingertips, until bubbles form and do not deflate. \n 10: Then, stretch and press the dough into a thin round. Make it thinner than you think it should be, as it will slightly shrink and puff up during baking. \n 11: Sprinkle 1/4 cup semolina onto an upside down baking sheet and place the stretched crust onto it. Add the sauce, mozzarella cheese, and any other toppings of your choice. \n 12: Slide the pizza onto the preheated pizza stone or pan. Bake for 15 minutes, or until the crust and cheese are golden brown. \n 13: Add any garnish of your preference.')

    session.add_all([cookie_recipe, blt_recipe, pizza_recipe])
    session.commit()

    cookie_ingredient_ids = [3,4,6,7,8,9,15]
    blt_ingredient_ids = [10,11,12,13,14]
    pizza_ingredient_ids = [1,4,7,16,17,18,19,20,21]
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
    for i in pizza_ingredient_ids:
        session.add(RecipeIngredient(
            ingredient_id = i,
            recipe_id = 3
        ))
    session.commit()

    fridge1 = Fridge(user='Marc')
    fridge2 = Fridge(user='Shanley')
    fridge3 = Fridge(user='Sadaf')
    session.add_all([fridge1, fridge2, fridge3])
    session.commit()

    pizza_ingredients = Recipe.get_recipe('Pizza').ingredients
    for i in pizza_ingredients:
        fi = FridgeIngredient(
            fridge_id = fridge2.id,
            ingredient_id = i.id
        )
        session.add(fi)
    session.commit()

    cookies_ingredients = Recipe.get_recipe('Chocolate Chip Cookies').ingredients
    for i in cookies_ingredients:
        ci = FridgeIngredient(
            fridge_id = fridge3.id,
            ingredient_id = i.id
        )
        session.add(ci)
    session.commit()

    blt_ingredients = Recipe.get_recipe('BLT').ingredients
    for i in blt_ingredients:
        blti = FridgeIngredient(
            fridge_id = fridge1.id,
            ingredient_id = i.id
        )
        session.add(blti)
    session.commit()
    
    session.close()