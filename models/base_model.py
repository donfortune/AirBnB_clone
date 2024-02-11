#!/usr/bin/python3

from uuid import uuid4
from datetime import datetime
import models

class BaseModel:
    """BaseModel class
    
    This class represents the base model for all other models in the application.
    """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs:  
            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = str(uuid4())
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of BaseModel"""
        return '[{}] ({}) {}'.format(type(self).__name__,self.id, self.__dict__)

    def save(self):
        """Save BaseModel instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Return dictionary representation of BaseModel"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = type(self).__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

if __name__ == '__main__':
    pass  # Add any additional code for script execution here

