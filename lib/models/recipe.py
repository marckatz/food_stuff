from sqlalchemy import Column, String, Integer
from foodstuff import Base, session
from sqlalchemy.orm import relationship

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer(), primary_key=True)
    directions = Column(String())

    recipe_ingredients = relationship('RecipeIngredient', cascade='all, delete-orphan')