#!/usr/bin/python3
"""defines state class and an instanse of sqlAlchemy Base"""
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)


user = 'user1'
passwd = 'Pass@123'
engine = create_engine(f'mysql+mysqlconnector://\
            {user}:{passwd}@localhost:3306/hbtn_0e_usa')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()
