#!/usr/bin/python3
"""defines all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <mysql password> \
				    <mysql username> \
                                    <database name>
"""

import sys
from model_state import State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()

    result = session.query(State).order_by(State.id).all()
    for state in result:
        print("{}: {}".format(state.id, state.name))
