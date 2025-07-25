#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, Integer, Text, String, create_engine, Foreignkey, Datetime
from sqlalchemy.orm import declarative_base, relationship, sessionmaker

Base = declarative_base()

class BaseModel:
    """A base class for all hbnb models"""

      id = Column(String(60), uuid.uuid4(), primarykey = True)
      created_at = Column(DateTime, default = datetime.utcnow(), nullable = False)
      updated_at = Column(DateTime, default = datetime.utcnow(), nullable = False)

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        if not kwargs:
            from models import storage
            self.id = Column(String(60), uuid.uuid4(), primarykey = True)
            self.created_at = Column(DateTime, default = datetime.utcnow(), nullable = False)
            self.updated_at = Column(DateTime, default = datetime.utcnow(), nullable = False)
        else:
            kwargs['updated_at'] = datetime.strptime(kwargs['updated_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            kwargs['created_at'] = datetime.strptime(kwargs['created_at'],
                                                     '%Y-%m-%dT%H:%M:%S.%f')
            del kwargs['__class__']
            self.__dict__.update(kwargs)

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()


    def to_dict(self):
        """Convert instance into dict format"""
        dictionary = {}
        dictionary.update(self.__dict__)
        dictionary.update({'__class__':
                          (str(type(self)).split('.')[-1]).split('\'')[0]})
        dictionary['created_at'] = self.created_at.isoformat()
        dictionary['updated_at'] = self.updated_at.isoformat()
        return dictionary
