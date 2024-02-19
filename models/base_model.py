#!/usr/bin/python3
"""
Module BaseModel
(Parent of all classes)
"""
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """Base class for Airbnb clone project
    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *arg, **kwargs):
        """
        Initialize attributes: random uuid, dates created/updated
        """
        if kwargs:
            for key, val in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        "%Y-%m-%dT%H:%M:%S.%f")
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, val)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """
        Return string representation of BaseModel instance.
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def to_dict(self):
        """
        Return dictionary containing all key/values of the __dict__ instance;
         and add class info to dic
        """
        dic = {}
        dic["__class__"] = self.__class__.__name__
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic

    def save(self):
        """Update the public instance attribute
        updated_at with the current datetime."""
        self.updated_at = datetime.now()
        models.storage.save()

    def __repr__(self):
        """
        Returns string representation
        """
        return (self.__str__())
