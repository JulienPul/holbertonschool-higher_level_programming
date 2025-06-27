#!/usr/bin/python3
"""
Script that prints the State.id of a State object with the name
passed as argument from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_id_by_name(username, password, db_name, state_name):
    """
    Prints the id of the State object matching the given name.
    If not found, prints 'Not found'.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()
    if state:
        print(state.id)
    else:
        print("Not found")


if __name__ == "__main__":
    if len(sys.argv) == 5:
        get_state_id_by_name(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
