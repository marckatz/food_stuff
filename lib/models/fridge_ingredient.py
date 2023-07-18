from sqlalchemy import Column, Integer 
from ..foodstuff import Base, session

class FridgeIngredient(Base):
    __tablename__ = 'fridge_ingredients'

    id = Column(Integer(), primary_key=True)
    recipe_id = Column(Integer())
    ingredient_id = Column(Integer())