#!/usr/bin/python3
"""
Script that adds the State object 'Louisiana' to the database hbtn_0e_6_usa.
Prints the id of the new State after creation.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def add_state_louisiana(username, password, db_name):
    """
    Adds 'Louisiana' to the states table and prints its id.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print(new_state.id)


if __name__ == "__main__":
    if len(sys.argv) == 4:
        add_state_louisiana(sys.argv[1], sys.argv[2], sys.argv[3])
