from config.base import engine , Base

def create_table():
    Base.metadata.create_all(engine)

def drop_tables():
    Base.metadata.drop_all(engine)