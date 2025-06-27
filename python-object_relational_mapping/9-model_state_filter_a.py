#!/usr/bin/python3
"""
Script that lists all State objects containing the letter a
from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def list_states_with_a(username, password, db_name):
    """
    Lists all State objects from the database that contain the letter 'a'
    and prints them ordered by id ascending.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)

    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])
