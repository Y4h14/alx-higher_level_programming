#!/usr/bin/python3
"""
Start link class to table in database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State, Base
import sys


if __name__ == "__main__":
    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.createall(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).all()
    for item in result:
        print(f'{item.id}: {item.name}')
