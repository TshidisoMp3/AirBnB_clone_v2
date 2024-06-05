#!/usr/bin/python3
"""This module explains a class to manage db storage for hbnb clone"""


from os import getenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


classes203 = { 'User': User, 'State': State, 'City': City, 'Place': Place, 'Amenity': Amenity, 'Review': Review }


class DBStorage:
    """This class operates as the storage engine for hbnb clone"""
    __engine = None
    __session = None

    def __init__(self):
        """This method initializes the DBStorage class"""
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(getenv('HBNB_MYSQL_USER'),
                                              getenv('HBNB_MYSQL_PWD'),
                                              getenv('HBNB_MYSQL_HOST'),
                                              getenv('HBNB_MYSQL_DB')),
                                      pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)
    
    def all(self, cls=None):
        """This method queries the current database session"""
        new_dict = {}
        if cls:
            if type(cls) == str:
                cls = classes203[cls]
            for obj in self.__session.query(cls):
                key = obj.__class__.__name__ + '.' + obj.id
                new_dict[key] = obj
        else:
            for name, cls in classes203.items():
                for obj in self.__session.query(cls):
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return new_dict
    
    def new(self, obj):
        """This method adds the object to the current database session"""
        self.__session.add(obj)
    
    def save(self):
        """This method commits all changes of the current database session"""
        self.__session.commit()
    
    def delete(self, obj=None):
        """This method deletes from the current database session"""
        if obj:
            self.__session.delete(obj)
    
    def reload(self):
        """This method creates all tables in the database"""
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        self.__session = scoped_session(Session)
    
    def close(self):
        """This method closes the current session"""
        self.__session.remove()
    