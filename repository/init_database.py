from returns.result import Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import engine, Base, session_factory


# def create_table():
#     Base.metadata.create_all(engine)
#
# def drop_tables():
#     Base.metadata.drop_all(engine)


def create_table():
    create_my_table("""
        create table if not exists Countries (
            country_id serial primary key,
            country_name varchar(100) unique not null
        );
        """)
    create_my_table(
        '''
        create table if not exists Cities (
            city_id serial primary key,
            city_name varchar(100) unique not null,
            country_id int not null,
            latitude decimal,
            longitude decimal,
            foreign key (country_id) references Countries(country_id)
        );
        '''
    )
    create_my_table('''
        create table if not exists TargetTypes (
            target_type_id serial primary key,
            target_type_name varchar(255) unique not null
        );
    ''')
    create_my_table('''
        create table if not exists Targets (
            target_id serial primary key,
            target_industry varchar(255) not null,
            city_id int not null,
            target_type_id int,
            target_priority int,
            foreign key (city_id) references Cities(city_id),
            foreign key (target_type_id) references TargetTypes (target_type_id)
        );
    ''')

def create_my_table(string:str):
    with session_factory() as session:
        try:
            session.execute(string)
            session.commit()
            return Success
        except SQLAlchemyError as e:
            return Failure(str(e))

