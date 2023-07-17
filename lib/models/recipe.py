from sqlalchemy import Column, String, Integer
from foodstuff import Base, session
from sqlalchemy.orm import relationship

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    directions = Column(String())

    recipe_ingredients = relationship('RecipeIngredient', cascade='all, delete-orphan')

    def __repr__(self):
        return f'<Recipe {self.id}: {self.name}>'