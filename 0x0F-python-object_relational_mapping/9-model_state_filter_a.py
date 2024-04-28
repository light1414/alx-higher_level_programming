#!/usr/bin/python3
"""Defines all State objects that contain the letter a
from the database hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py <mysql password> /
				   <mysql username> /
                                   <database name>
"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == '__main__':
    # Start connection to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # start a configured "Session" class
    Session = sessionmaker(bind=engine)

    # start a Session instance
    session = Session()

    # prompt the database for all State objects that contain the letter "a"
    states_with_a = session.query(State).filter(State.name.like('%a%')).\
        order_by(State.id)

    # display the results
    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    # end session
    session.close()
