from sqlalchemy import Column, String, Integer
from ..foodstuff import Base, session
from sqlalchemy.orm import relationship

class Ingredient(Base):
    __tablename__ = 'ingredients'

    id = Column(Integer(), primary_key=True)
    name = Column(String())

    recipe_ingredients = relationship('RecipeIngredient', cascade='all, delete-orphan')
    fridge_ingredients = relationship('FridgeIngredient', cascade='all, delete-orphan')

    @property
    def recipes(self):
        return [ri.recipe for ri in self.recipe_ingredients]

    @classmethod
    def get_ingredient(cls, ingredient_name):
        return session.query(cls).filter(cls.name == ingredient_name).first()

    def __repr__(self):
        return f'<Ingredient {self.id}: {self.name}>'
    
    def __str__(self):
        return self.name