from sqlalchemy import Column, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///food_stuff.db')

Base = declarative_base()

class FridgeIngredient(Base):
    __tablename__ = 'fridge_ingredients'

    id = Column(Integer(), primary_key=True)
    recipe_id = Column(Integer())
    ingredient_id = Column(Integer())