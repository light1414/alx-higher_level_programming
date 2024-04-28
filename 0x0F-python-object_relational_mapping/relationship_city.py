#!/usr/bin/python3
"""lists a City model.
takes from SQLAlchemy Base and links to the MySQL table cities.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, ForeignKey, Integer, String

Base = declarative_base()


class City(Base):
    """Reps a city for MySQL dataabase.
    Attributes:
        id (sqlalchemy.Column): City's id.
        name (sqlalchemy.Column): City's name.
        state_id (sqlalchemy.Column): The city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
