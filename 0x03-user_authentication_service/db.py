#!/usr/bin/env python3
"""DB module
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.exc import InvalidRequestError

from user import Base, User


class DB:
    """DB class
    """

    def __init__(self) -> None:
        """Initialize a new DB instance
        """
        self._engine = create_engine("sqlite:///a.db", echo=True)
        Base.metadata.drop_all(self._engine)
        Base.metadata.create_all(self._engine)
        self.__session = None

    @property
    def _session(self) -> Session:
        """Memoized session object
        """
        if self.__session is None:
            DBSession = sessionmaker(bind=self._engine)
            self.__session = DBSession()
        return self.__session

    def add_user(self, email: str, hashed_password: str) -> User:
        """Save a user to the database"""
        auser = User(email=email, hashed_password=hashed_password)
        self._session.add(auser)
        self._session.commit()
        return auser

    def find_user_by(self, **kwargs: dict) -> User:
        """Returns the first row found in the user tables as filtered
        by the method's input arguments
        """
        try:
            auser = self._session.query(User).filter_by(**kwargs).one()
        except NoResultFound:
            raise
        except InvalidRequestError:
            raise
        return auser

    def update_user(self, user_id: int, **kwargs: dict) -> None:
        """Uses find_user_by to locate the user to update then update
        the user's attribute as passed in the method's arguments
        """
        try:
            auser = self.find_user_by(id=user_id)
            for k, v in kwargs.items():
                auser.__setattr__(k, v)
            self.__session.add(auser)
            self.__session.commit()
        except ValueError:
            raise
