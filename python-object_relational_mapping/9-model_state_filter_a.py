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
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+pymysql://{username}:{password}@localhost:3306/{database}",
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    results = session.query(State) \
        .filter(State.name.like('%a%')) \
        .order_by(State.id)

    for state in results:
        print(f"{state.id}: {state.name}")
