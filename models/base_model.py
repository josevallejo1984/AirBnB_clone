#!/usr/bin/python3
"""Create class BaseModel that defines all common 
attributes/methods for other class
"""
import models
from uuid import uuid4
from datetime import datetime

class BaseModel(object):
    """Define class BaseModel"""
    def __init__(self, *args, **kwargs):
        """Initialized constructor"""
        time_form = "%Y-%m-%dT%H:%M:%S.%f"     
        self.id = str(uuid4())
        self.updated_at = datetime.today()
        self.created_at = datetime.today()
        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    self.__dict__[k] = datetime.strptime(v, time_form)
                else:
                    self.__dict__[k] = v
    
    def save(self):
        """updates the public instance attributes with the current datetime
        """
        self.updated_at = datetime.today()
    
    def to_dict(self):
        """ returns a dictionary containing all keys/values of 
        __dict__ of the instance
        """
        new_dict = self.__dict__.copy()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["__class__"] = self.__class__.__name__
        return new_dict
    
    def __str__(self):
        """print string"""
        class_name = self.__class__.__name__
        return '[{}] ({}) {}'.format(class_name, self.id, self.__dict__)

