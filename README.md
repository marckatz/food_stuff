Welcome to Pantry Planner!

RecipeFinder is a CLI where you, the user, can interact with your virtual fridge in order to plan out your meals. You can add ingredients to your fridge, create new recipes, and see what recipes you can make with the ingredients that you have in your fridge!

To run Pantry Planner, 
Clone down the repo, run: pipenv install and pipenv shell, and then type: python pantry_planner.py in the command line. 

When you first enter our interface, the prompt will ask you for your username. This is how you will keep the items in your fridge separate from the items in other users' fridges. 

If you don't have a username set up already, just type in your name and it will automatically create your very own fridge!

After you're in your fridge, you can search around using these commands:
-add recipe 
    This will prompt you to add the new recipe name, and then the new recipe directions to add a new recipe into our database.
-add ingredient 
    Add your new recipe's ingredients to our ingredients table.
-add ingredient to recipe
    This will prompt you to specify which ingredient from our ingredient's database you want to add to a recipe, then it will prompt you to specify the recipe name you are adding it to. If the ingredient does not currently exist in our database, it will create the new ingredient in our database for you. 
-remove ingredient from recipe
    This will prompt you to specify which ingredient from our ingredient's database you want to remove from a recipe, then it will prompt you to specify the recipe name you are removing the ingredient from.
-update recipe
    This will prompt you to enter a recipe's name, then you can see the previous directions, then it sill prompt you to enter the new directions for the recipe.
-show all recipes
    Returns a list of all the recipes that are already in our database.
-search recipe by ingredient
    This will prompt you to specify which ingredients you want to search by for recipes.
-search recipe
    This will prompt you to enter a recipe name and it will search our database and return the recipe that matches.
-search ingredient
    This will prompt you to enter an ingredient name and it will tell you if the ingredient is or is not currently in the database.
-open fridge
    Shows the ingredients that are in the current user's fridge.
-add ingredient to fridge
    Will prompt you to enter whatever ingredient you want to have in your fridge. If the ingredient does not already exist, it will create the new ingredient in our database for you.
-remove ingredient from fridge
    Will prompt you to enter the name of the ingredient that you want to remove from your fridge.
-get available recipes
    Will search through the ingredients in your fridge and return what recipes you can make with the ingredients that are in your fridge. If there are no available recipes, it will let you know that you can't make anything with what is in your fridge and to add more ingredients to your fridge in order to see some recipes.
-swap user
    Swaps the current user.
-close
    Exits the program.
-help
    Returns a list of all commands.

Thanks for using Pantry Planner!

Authors: Marc Katz, Sadaf Chadwick, Shanley Caswell