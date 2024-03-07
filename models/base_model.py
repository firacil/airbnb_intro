#!/usr/bin/python3
import uuid
from datetime import datetime
""" Class to implement base"""


class BaseModel:
    """ class defines all common attr/methods"""

    def __init__(self, *args, **kwargs):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ print: class name, id, dict"""
        return ("[{}] ({}) {}".
                format(self.__class__.__name__, self.id, self.__dict__)
                )

    def save(self):
        """ update updated_at attr with current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """ return dictionary representation of BaseModel"""
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = self.__class__.__name__
        new_dict['created_at'] = self.created_at.isoformat()
        new_dict['updated_at'] = self.updated_at.isoformat()
        return new_dict
