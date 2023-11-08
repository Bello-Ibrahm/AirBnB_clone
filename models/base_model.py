#!/usr/bin/python3
"""Base class module definition for all models in hbnb clone"""

import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """Base class"""

    def __init__(self, *args, **kwargs):
        """instantiates a new model

        Attributes:
            *args (any): Unused.
            **kwargs (dict): Key/pairs of attributes.
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for i in kwargs:
                if i in ['created_at', 'updated_at']:
                    setattr(self, i, datetime.fromisoformat(kwargs[i]))
                elif i != '__class__':
                    setattr(self, i, kwargs[i])

    def __str__(self):
        """Returns a string representation of the instance"""
        return ('[{}] ({}) {}'.format(
            self.__class__.__name__, self.id, self.__dict__))

    def save(self):
        """Updates the update_at with current time when instance changed"""
        self.update_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        for j in dct:
            if type(dct[j]) is datetime:
                dct[j] = dct[j].isoformat()
        if ('_sa_instance_state' in dct.keys()):
            del(dct['_sa_instance_state'])
        return (dct)
