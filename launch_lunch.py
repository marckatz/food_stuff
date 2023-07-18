#!/usr/bin/env python3
from lib.models import *
from lib.foodstuff import session

if __name__=='__main__':
    print("Welcome to the program")
    user_input = ""
    while user_input != 'close':
        user_input = input("What do you want to do?\n> ")
        if user_input == "add ingredient":
            ingredient_name = input("Ingredient name:\n> ")
            ingredient = Ingredient(name=ingredient_name)
            session.add(ingredient)
            session.commit()
        
        elif user_input == "add recipe":
            recipe_name = input("Recipe name:\n> ")
            recipe_directions = input("Directions:\n> ")
            recipe = Recipe(name=recipe_name, directions=recipe_directions)
            session.add(recipe)
            session.commit()
        
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
            if recipe:
                print(recipe.name)
                print('Ingredients:')
                for i in recipe.ingredients:
                    print(i)
                print(recipe.directions)
            else:
                print(f'{recipe_name} not found ¯\_(ツ)_/¯')

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
            ingredient = Ingredient.get_ingredient(ingredient_name)
            recipe = Recipe.get_recipe(recipe_name)
            recipe.add_ingredient(ingredient)
            print(f'Added {ingredient_name} to {recipe_name}')
        
        elif user_input == "remove ingredient from recipe":
            #assume valid recipe and ingredient, and ingredient is in recipe
            ingredient_name = input("Enter ingredient name:\n> ")
            recipe_name = input("Enter recipe name:\n> ")
            ingredient = Ingredient.get_ingredient(ingredient_name)
            recipe = Recipe.get_recipe(recipe_name)
            recipe.remove_ingredient(ingredient)
            print(f'Removed {ingredient_name} from {recipe.name}')


        elif user_input == "help":
            print("ask Emiley")


        elif user_input != "close":
            print("Invalid input dummy")