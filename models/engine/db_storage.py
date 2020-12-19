#!/usr/bin/python3
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import scoped_session
from sqlalchemy import (create_engine)
import os
from models.amenity import Amenity
from models.state import State
from models.city import City
from models.review import Review
from models.user import User
from models.place import Place
from models.base_model import Base


class DBStorage():
    """New engine DBStorage"""
    __engine = None
    __session = None

    def __init__(self):
        """Constructor"""

        user = os.getenv("HBNB_MYSQL_USER")
        passwd = os.getenv("HBNB_MYSQL_passwd")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        connection = 'mysql+mysqldb://{}:{}@localhost/{}'
        self.__engine = create_engine(connection.format(
            user, passwd, db), pool_pre_ping=True)
        if (os.getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """The dictionary of cls"""
        new_dict = {}
        if cls:
            query = self.__session.query(eval(cls))
            for class_ in query:
                key = "{}.{}".format(type(class_).__name__, class_.id)
                new_dict[key] = class_
        else:
            class_list = [User, State, City, Amenity, Place, Review]
            for class_ in class_list:
                query = self.__session.query(class_)
                for obj in query:
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """New object to db"""
        self.__session.add(obj)

    def save(self):
        """Commit  the objetc to db"""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """
        create all tables in the database
        """
        # create tables into a db
        Base.metadata.create_all(self.__engine)
        # creamos el session object
        # expire_on_commmot = false >>> ignore the query sql
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()