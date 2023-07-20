from sqlalchemy import Column, String, Integer
if 'lib' in __name__:
    from lib.foodstuff import Base, session
else:
    from foodstuff import Base, session
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
    
    def add_ingredient(self, ingredient):
        from .recipe_ingredient import RecipeIngredient
        ri = RecipeIngredient(
            recipe_id = self.id,
            ingredient_id = ingredient.id
        )
        session.add(ri)
        session.commit()

    #only removes first instance of <ingredient>
    def remove_ingredient(self, ingredient):
        from .recipe_ingredient import RecipeIngredient
        ri = session.query(RecipeIngredient).filter(
            RecipeIngredient.ingredient_id == ingredient.id,
            RecipeIngredient.recipe_id == self.id).first()
        if ri:
            session.delete(ri)
            session.commit()
        else:
            raise Exception(f'{str(ingredient)} is not in {str(self)}')

    def update_directions(self, new_directions):
        self.directions = new_directions
        session.commit()

    @classmethod
    def get_recipe(cls, recipe_name):
        return session.query(cls).filter(cls.name == recipe_name).first()
    
    @classmethod
    def all(cls):
        return session.query(cls).all()

    def __repr__(self):
        return f'<Recipe {self.id}: {self.name}>'
    
    def __str__(self):
        return self.name