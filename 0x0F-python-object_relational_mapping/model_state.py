#!/usr/bin/python3
"""defines state class and an instanse of sqlAlchemy Base"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql://\'user1\':\'Pass123\'}@localhost:3306/hbtn_0d_usa', echo=True)


Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)



Base.metadata.create_all(bind=engine)
