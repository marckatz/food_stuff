#!/usr/bin/env python3
import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

#from <file> import <class>

if __name__=='__main__':
    engine = create_engine('sqlite:///../food_stuff.db')
    Session = sessionmaker(bind=engine)
    session = Session()

    ingredients = session.query(Ingredient).all()
    recipes = session.query(Recipe).all()
    recipe_ingredients = session.query(RecipeIngredient).all()

    ipdb.set_trace()

    session.close()