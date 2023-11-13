#!/usr/bin/python3
"""Base class module definition for all models in hbnb clone"""

import uuid
import models
from datetime import datetime
<<<<<<< HEAD
=======

>>>>>>> 196822e5b6c7f0583045a0aece70690fdec0fc90

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
            self.created_at = datetime.today()
            self.updated_at = datetime.today()
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
<<<<<<< HEAD
        from models import storage
        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        for k in dct:
            if type(dct[k]) is datetime:
                dct[k] = dct[k].isoformat()
        if '_sa_instance_state' in dct.keys():
            del(dct['_sa_instance_state'])
        return dct

    def delete(self):
        '''deletes the current instance from the storage'''
        from models import storage
        storage.delete(self)
=======
        self.update_at = datetime.today()
        models.storage.save()

    def to_dict(self):
        """Return the dictionary of the BaseModel instance"""
        retdict = self.__dict__.copy()
        retdict["created_at"] = self.created_at.isoformat()
        retdict["updated_at"] = self.updated_at.isoformat()
        retdict["__class__"] = self.__class__.__name__
        return retdict
>>>>>>> 196822e5b6c7f0583045a0aece70690fdec0fc90
