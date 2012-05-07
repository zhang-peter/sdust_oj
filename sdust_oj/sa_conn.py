'''
Created on Apr 26, 2012

@author: jingyong
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:123456@localhost/mytest',echo=True)
DeclarativeBase = declarative_base()
metadata = DeclarativeBase.metadata
metadata.bind = engine


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)