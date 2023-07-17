from sqlalchemy import Column, Integer, Float, ForeignKey
from foodstuff import Base, session
from sqlalchemy.orm import relationship

class RecipeIngredient(Base):
    __tablename__ = 'recipe_ingredients'

    id = Column(Integer(), primary_key=True)
    recipe_id = Column(Integer(), ForeignKey('recipes.id'))
    ingredient_id = Column(Integer(), ForeignKey('ingredients.id'))
    #amount = Column(Float())

    recipe = relationship('Recipe', back_populates='recipe_ingredients')

    ingredient = relationship('Ingredient', back_populates='recipe_ingredients')