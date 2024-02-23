#!/usr/bin/python3
"""defines state class and an instanse of sqlAlchemy Base"""
from sqlalchemy import ForeignKey, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    Class for the city table
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
