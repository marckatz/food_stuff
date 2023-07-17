from sqlalchemy import Column, String, Integer
from foodstuff import Base, session
from sqlalchemy.orm import relationship

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    recipe_ingredients = relationship('RecipeIngredient', cascade='all, delete-orphan')