#!/usr/bin/python3
"""
Start link class to table in database
"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State.name,
                            City.id,
                            City.name).join(
                                State,
                                State.id == City.id
                                )
    for item in result:
        print(f"{item[0]}: ({item[1]}) {item[2]}")
