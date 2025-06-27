#!/usr/bin/python3
"""
Script that changes the name of the State object with id = 2
to 'New Mexico' in the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state_name(username, password, db_name):
    """
    Updates the State with id=2 to have the name 'New Mexico'.
    """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{db_name}",
        pool_pre_ping=True
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        update_state_name(sys.argv[1], sys.argv[2], sys.argv[3])
