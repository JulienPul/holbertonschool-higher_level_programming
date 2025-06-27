#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa
Usage: ./8-model_state_fetch_first.py <username> <password> <database>
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    # Get arguments from command line
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Create engine to connect to the database
    engine = create_engine(
        f'mysql+mysqldb://{username}:{password}@localhost:3306/{database}',
        pool_pre_ping=True
    )

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch the first State object by id
    first_state = session.query(State).order_by(State.id).first()

    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
