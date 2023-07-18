from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from ..foodstuff import Base, session

class Fridge(Base):
    __tablename__ = 'fridges'

    id = Column(Integer(), primary_key=True)
    user = Column(String())

    fridge_ingredients = relationship('FridgeIngredient', cascade='all, delete-orphan')

    @property
    def ingredients(self):
        return [fi.ingredient for fi in self.fridge_ingredients]
    
    def add_ingredient(self, ingredient):
        from .fridge_ingredient import FridgeIngredient
        fi = FridgeIngredient(
            ingredient_id = ingredient.id,
            fridge_id = self.id
        )
        session.add(fi)
        session.commit()

    def remove_ingredient(self, ingredient):
        fi = [fi for fi in self.fridge_ingredients if fi.ingredient == ingredient][0]
        session.remove(fi)
        session.commit()

    @classmethod
    def get_fridge(cls, username):
        return session.query(cls).filter(cls.user == username).first()
    
    def __repr__(self):
        return f'<Fridge {self.id}: {self.user}>'
        
