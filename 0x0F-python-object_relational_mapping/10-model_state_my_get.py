#!/usr/bin/python3
"""defines the State object with the name passed as argument
from the database hbtn_0e_6_usa.
Usage: ./10-model_state_my_get.py <mysql username> /
                                  <mysql password> /
                                  <state name searched>
                                  <database name>
"""
from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # start a link to the database.
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    # make a configured "Session" class.
    Session = sessionmaker(bind=engine)

    # make a Session object for our queries.
    session = Session()

    # prompt the database for the state with the specified name.
    sta = session.query(State).filter(State.name == sys.argv[4]).first()

    # display the state's ID or "Not found" if the state is not in the database.
    if state:
        print(sta.id)
    else:
        print("Not found")
