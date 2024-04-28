#!/usr/bin/python3
"""displays the first State object from the database hbtn_0e_6_usa.
Usage: ./8-model_state_fetch_first.py <mysql password> /
				      <mysql username> /
                                      <database name>
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # link to database
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, db_name),
                           pool_pre_ping=True)

    # start session
    Session = sessionmaker(bind=engine)
    session = Session()

    # prompt database for the first State object
    first_state = session.query(State).order_by(State.id).first()

    if first_state is None:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
