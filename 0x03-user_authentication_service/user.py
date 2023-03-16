#!/usr/bin/env python3
"""A user Uer model"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    """A user model with the attributes
    id: integer peimary key
    email: a non nullable string
    hashed_password: a non nullable string
    session_id: a nullable string
    reset_token: a nullable string
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
