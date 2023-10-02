import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()



class User(Base):
     __tablename__ = 'User'
     ID = Column(Integer, primary_key=True)
     username = Column(String(250))
     firstname = Column(String(250))
     lastname = Column(String(250))
     username = Column(String(250))
     email = Column(String(250))

class Character(Base):
    __tablename__ = 'Character'
    ID = Column(Integer, primary_key=True)
    character_name = Column(String(250))
    character_description = Column(String(250))

class Planet(Base):
    __tablename__ = 'Planet'
    ID = Column(Integer, primary_key=True)
    planet_name = Column(String(250))
    planet_description = Column(String(250))

class favourite_characters(Base):
    __tablename__ = 'Favourite Characters'
    ID = Column(Integer, primary_key=True)
    userId = Column(Integer, ForeignKey('User.ID'))
    favourite_character = Column(Integer, ForeignKey('Character.ID'))
    user = relationship(User)

class favourite_planets(Base):
    __tablename__ = 'Favourite Planets'
    ID = Column(Integer, primary_key=True)
    userID = Column(Integer, ForeignKey('User.ID'))
    favourite_planet = Column(Integer, ForeignKey('Planet.ID'))
    user = relationship(User)




# class Person(Base):
#     __tablename__ = 'person'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     name = Column(String(250), nullable=False)

# class Address(Base):
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Person)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
