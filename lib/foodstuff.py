from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

convention = {
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s'
}

engine = create_engine('sqlite:///food_stuff.db')
Session = sessionmaker( bind = engine )
session = Session()

md = MetaData(naming_convention = convention)
Base = declarative_base(metadata=md)