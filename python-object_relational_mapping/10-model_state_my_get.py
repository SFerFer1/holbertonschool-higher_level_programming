#!/usr/bin/python3
"""
hhijjhjstkks
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":

    if len(sys.argv) != 5:
        print("Usage: ./script.py <mysql username> <mysql password> <database name> <state name to search>")
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost/{database_name}',
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()
