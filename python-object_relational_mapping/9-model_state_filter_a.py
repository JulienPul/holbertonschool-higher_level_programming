#!/usr/bin/python3
"""
Lists all State objects that contain the letter 'a' from the database
hbtn_0e_6_usa.
Usage: ./9-model_state_filter_a.py <username> <password> <database>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get MySQL credentials and database name
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine and connect to the database
    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states that contain the letter 'a', ordered by id
    states_with_a = session.query(State) \
        .filter(State.name.like('%a%')) \
        .order_by(State.id)

    # Print results
    for state in states_with_a:
        print(f"{state.id}: {state.name}")
