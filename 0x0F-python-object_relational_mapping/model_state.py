#!/usr/bin/python3
"""lists a State model.
takes from SQLAlchemy Base and links to the MySQL table states.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class State(Base):
    """Reps a state for a MySQL database.
    __tablename__ (str): Name of the MySQL table to store States
    id (sqlalchemy.Integer): State's id.
    name (sqlalchemy.String): State's name.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
