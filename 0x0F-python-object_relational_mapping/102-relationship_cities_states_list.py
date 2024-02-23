#!/usr/bin/python3
"""
Start link class to table in database
"""
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import State, Base
import sys

if __name__ == "__main__":

    engine = create_engine(
        "mysql+mysqldb://{}:{}@localhost:3306/{}"
        .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State).order_by(State.id)
    for result in results:
        for city in result.cities:
            print(city.id, city.name, sep=": ", end="")
            print(" -> " + result.name)
