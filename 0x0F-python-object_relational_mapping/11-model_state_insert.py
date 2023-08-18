#!/usr/bin/python3
"""
Adds the State object “Louisiana” to the database hbtn_0e_6_usa
"""
if __name__ == "__main__":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    from model_state import Base, State
    from sys import argv

    if (len(argv) != 4):
        print('Use: username, password database_name')
        exit(1)
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    fresh_row = State(name='Louisiana')
    session.add(fresh_row)
    session.commit()

    states = session.query(State).where(State.name == 'Louisiana')
    for rows in states:
        print(rows.id)
    session.close()
