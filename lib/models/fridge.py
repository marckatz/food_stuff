from sqlalchemy import Column, String, Integer
from ..foodstuff import Base, session

class Fridge(Base):
    __tablename__ = 'fridges'

    id = Column(Integer(), primary_key=True)
    user = Column(String())