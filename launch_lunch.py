#!/usr/bin/env python3
from lib.models import *
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__=='__main__':
    engine = create_engine('sqlite:///food_stuff.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    print("Welcome to the program")
    user_input = ""
    while user_input != 'close':
        user_input = input("What do you want to do?\n> ")
        if user_input == "add ingredient": #input will include ingredient name
            ingredient_name = input("Ingredient name:\n> ")
            ingredient = Ingredient(name=ingredient_name)
            session.add(ingredient)
            session.commit()
        
        elif user_input == "add recipe":
            recipe_name = input("Recipe name:\n> ")
            recipe_directions = input("Directions:\n> ")
            recipe = Recipe(name=recipe_name, directions=recipe_directions)
            #add recipe to database
        
        elif user_input == "search recipe by ingredient":
            ingredient_inputs = input("Enter ingredients:\n> ")
            #assume all ingredients are valid
            ingredient_list = [Ingredient.get_ingredient(i.strip()) for i in ingredient_inputs.split(',')]
            recipes = [recipe for recipe in Recipe.all() if all(i in recipe.ingredients for i in ingredient_list)]
            if len(recipes) > 0:
                print("You can cook:")
                for r in recipes:
                    print(r)
            else:
                print("You can't cook anything with those :(")
        
        elif user_input == "search recipe":
            recipe_name = input("Enter recipe name:\n> ")
            recipe = Recipe.get_recipe(recipe_name)
            print(recipe.name)
            print('Ingredients:')
            for i in recipe.ingredients:
                print(i)
            print(recipe.directions)

        elif user_input == "search ingredient":
            ingredient_name = input("Enter ingredient name:\n> ")
            ingredient = Ingredient.get_ingredient(ingredient_name)
            if ingredient:
                print(f'{str(ingredient)} is in the database')
            else:
                print(f'{ingredient_name} not found ¯\_(ツ)_/¯')

        elif user_input == "add ingredient to recipe":
            #assume valid recipe and ingredient
            ingredient_name = input("Enter ingredient name:\n> ")
            recipe_name = input("Enter recipe name:\n> ")
        
        elif user_input == "help":
            print("ask emiley")


        elif user_input != "close":
            print("Invalid input dummy")