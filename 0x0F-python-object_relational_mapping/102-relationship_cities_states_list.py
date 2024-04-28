#!/usr/bin/python3
"""difines all City objects from the database hbtn_0e_101_usa.
Usage: ./102-relationship_cities_states_list.py <mysql username> /
                                                <mysql password> /
                                                <database name>
"""

from sqlalchemy import create_engine
from relationship_city import City
from sqlalchemy.orm import sessionmaker
import sys
from relationship_state import State

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    for citi in session.query(City).order_by(City.id):
        print("{}: {} -> {}".format(citi.id, citi.name, citi.state.name))
