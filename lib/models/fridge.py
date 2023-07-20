from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
if 'lib' in __name__:
    from lib.foodstuff import Base, session
else:
    from foodstuff import Base, session

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
        fi = [fi for fi in self.fridge_ingredients if fi.ingredient == ingredient]
        if len(fi) > 0:
            fi = fi[0]
            session.delete(fi)
            session.commit()
        else:
            raise Exception(f'{str(ingredient)} is not in {self.user}\'s fridge')

    @classmethod
    def get_fridge(cls, username):
        user_fridge = session.query(cls).filter(cls.user == username).first()
        if not user_fridge:
            user_fridge = Fridge(user = username)
            session.add(user_fridge)
            session.commit()
        return user_fridge

    def __repr__(self):
        return f'<Fridge {self.id}: {self.user}>'
        
