#!/usr/bin/env python3
import ipdb
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import *

#from <file> import <class>

if __name__=='__main__':
    engine = create_engine('sqlite:///factorio.db')
    Session = sessionmaker(bind=engine)
    session = Session()


    ipdb.set_trace()

    session.close()