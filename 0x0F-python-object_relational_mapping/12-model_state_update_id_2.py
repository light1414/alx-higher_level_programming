#!/usr/bin/python3
"""replace the name of the State object with id = 2 to
New Mexico in the database hbtn_0e_6_usa.
Usage: ./12-model_state_update_id_2.py <mysql username> /
                                       <mysql password> /
                                       <database name>
"""

from sqlalchemy.orm import sessionmaker
import sys
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    # make a connection to the database
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    # prompt the State with id=2 and update its name to "New Mexico"
    new_state = session.query(State).filter(State.id == 2).first()
    if state:
        new_state.name = "New Mexico"
        session.commit()
    else:
        print("Not found")
    session.close()
