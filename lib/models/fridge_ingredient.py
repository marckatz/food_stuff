from sqlalchemy import Column, Integer, ForeignKey 
from sqlalchemy.orm import relationship 
if 'lib' in __name__:
    from lib.foodstuff import Base, session
else:
    from foodstuff import Base, session


class FridgeIngredient(Base):
    __tablename__ = 'fridge_ingredients'

    id = Column(Integer(), primary_key=True)
    fridge_id = Column(Integer(), ForeignKey('fridges.id'))
    ingredient_id = Column(Integer(), ForeignKey('ingredients.id'))

    fridge = relationship('Fridge', back_populates='fridge_ingredients')

    ingredient = relationship('Ingredient', back_populates='fridge_ingredients')

    def __repr__(self):
        return f'<FridgeIngredient {self.id}: Fridge {self.fridge.user}, Ingredient {self.ingredient.name}>'