#!/usr/bin/env python3
from lib.models import *
from lib.foodstuff import session

if __name__=='__main__':
    print("Welcome to Pantry Planner!")
    login = input("Enter Name:\n> ")
    current_fridge = Fridge.get_fridge(login)
    user_input = ""
    while user_input != 'close':
        user_input = input("\nWhat do you want to do?\n> ").strip().lower()

        if user_input == "add ingredient":
            ingredient_name = input("Ingredient name:\n> ")
            ingredient = Ingredient.get_ingredient(ingredient_name, add_otherwise=True)

        elif user_input == "add recipe":
            recipe_name = input("Recipe name:\n> ")
            recipe_directions = input("Directions:\n> ")
            recipe = Recipe(name=recipe_name, directions=recipe_directions)
            session.add(recipe)
            session.commit()

        elif user_input == "show all recipes":
            for recipe in Recipe.all():
                print(str(recipe))

        elif user_input == "search recipe by ingredient":
            ingredient_inputs = input("Enter ingredients:\n> ")
            ingredient_list = [Ingredient.get_ingredient(i.strip()) for i in ingredient_inputs.split(',')]
            recipes = [recipe for recipe in Recipe.all() if all(i in recipe.ingredients for i in ingredient_list)]
            if len(recipes) > 0:
                print("You can cook:")
                for r in recipes:
                    print(str(r))
            else:
                print("You can't cook anything with those :(")

        elif user_input == "search recipe":
            recipe_name = input("Enter recipe name:\n> ")
            recipe = Recipe.get_recipe(recipe_name)
            if recipe:
                print(recipe.name)
                print('Ingredients:')
                for i in recipe.ingredients:
                    print(str(i))
                print(recipe.directions)
            else:
                print(f'"{recipe_name}" not found ¯\_(ツ)_/¯')

        elif user_input == "search ingredient":
            ingredient_name = input("Enter ingredient name:\n> ")
            ingredient = Ingredient.get_ingredient(ingredient_name)
            if ingredient:
                print(f'{str(ingredient)} is in the database')
            else:
                print(f'"{ingredient_name}" not found ¯\_(ツ)_/¯')

        elif user_input == "add ingredient to recipe":
            recipe_name = input("Enter recipe name:\n> ")
            ingredient_name = input("Enter ingredient name:\n> ")
            recipe = Recipe.get_recipe(recipe_name)
            if recipe:
                ingredient = Ingredient.get_ingredient(ingredient_name, add_otherwise=True)
                recipe.add_ingredient(ingredient)
                print(f'Added {ingredient_name} to the {recipe_name} recipe')
            else:
                print(f'"{recipe_name}" not found ¯\_(ツ)_/¯')

        elif user_input == "remove ingredient from recipe":
            ingredient_name = input("Enter ingredient name:\n> ")
            recipe_name = input("Enter recipe name:\n> ")
            ingredient = Ingredient.get_ingredient(ingredient_name)
            recipe = Recipe.get_recipe(recipe_name)
            if recipe:
                try:
                    recipe.remove_ingredient(ingredient)
                    print(f'Removed {ingredient_name} from {recipe_name}')
                except Exception as e:
                    print(e)
            else:
                print(f'"{recipe_name}" not found ¯\_(ツ)_/¯')

        elif user_input == "update recipe":
            recipe_name = input("Enter recipe name:\n> ")
            recipe = Recipe.get_recipe(recipe_name)
            if recipe:
                print("Old recipe directions:")
                print(recipe.directions)
                new_recipe_directions = input("Enter new recipe directions:\n> ")
                recipe.update_directions(new_recipe_directions)
                print("Updated recipe")
            else:
                print(f'"{recipe_name}" not found ¯\_(ツ)_/¯')

        elif user_input == "help":
            print("Commands: \nadd ingredient\nadd recipe\nshow all recipes\nsearch recipe by ingredient\nsearch recipe\nsearch ingredient\nadd ingredient to recipe\nremove ingredient from recipe\nupdate recipe\nopen fridge\nadd ingredients to fridge\nremove ingredient from fridge\nget available recipes\nswap user\nclose")

        elif user_input == "open fridge":
            for i in current_fridge.ingredients:
                print(str(i))

        elif user_input == "add ingredients to fridge":
            ingredient_inputs = input("Enter ingredients:\n> ")
            ingredient_list = [Ingredient.get_ingredient(i.strip(), add_otherwise=True) for i in ingredient_inputs.split(',')]
            for ingredient in ingredient_list:
                current_fridge.add_ingredient(ingredient)
                print(f'Added {ingredient.name} to {current_fridge.user}\'s fridge!')

        elif user_input == "remove ingredient from fridge":
            ingredient_name = input("Enter ingredient name:\n> ")
            ingredient = Ingredient.get_ingredient(ingredient_name)
            if ingredient:
                try:
                    current_fridge.remove_ingredient(ingredient)
                    print(f'Removed {str(ingredient)}')
                except Exception as e:
                    print(e)
            else:
                print(f'"{ingredient_name}" is not valid')

        elif user_input == "get available recipes":
            recipes = [recipe for recipe in Recipe.all() if all(i in current_fridge.ingredients for i in recipe.ingredients)]
            if len(recipes) > 0:
                print("You can cook:")
                for r in recipes:
                    print(str(r))
            else:
                print("You can't make anything with what's in your fridge :(\nAdd some more ingredients to your fridge to see some recipes!")

        elif user_input == "swap user":
            login = input("Enter Name:\n> ")
            current_fridge = Fridge.get_fridge(login)
            print(f'Welcome to your fridge, {login}!')


        elif user_input != "close":
            print("Invalid input dummy")


    print("Bye bye!")