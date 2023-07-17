from sqlalchemy import Column, String, Integer, create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('sqlite:///food_stuff.db')

Base = declarative_base()

class Fridge(Base):
    __tablename__ = 'fridges'

    id = Column(Integer(), primary_key=True)
    user = Column(String())