#!/usr/bin/python3
"""Create a class City"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """class city with class attribute id, name, state_id"""
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128))
    state_id = Column(Integer, ForeignKey('states.id'))
