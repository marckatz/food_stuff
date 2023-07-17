from sqlalchemy import Column, String, Integer
from ..foodstuff import Base, session
from sqlalchemy.orm import relationship

class Recipe(Base):
    __tablename__ = 'recipes'

    id = Column(Integer(), primary_key=True)
    name = Column(String())
    directions = Column(String())

    recipe_ingredients = relationship('RecipeIngredient', cascade='all, delete-orphan')

    @property
    def ingredients(self):
        return [ri.ingredient for ri in self.recipe_ingredients]
    
    def add_ingredient(self, ingredient, amount, unit):
        from .recipe_ingredient import RecipeIngredient
        ri = RecipeIngredient(
            recipe_id = self.id,
            ingredient_id = ingredient.id,
            amount = amount,
            unit = unit
        )
        session.add(ri)
        session.commit()

    @classmethod
    def get_recipe(cls, recipe_name):
        return session.query(cls).filter(cls.name == recipe_name).first()
    
    @classmethod
    def all(cls):
        return session.query(cls).all()

    def __repr__(self):
        return f'<Recipe {self.id}: {self.name}>'