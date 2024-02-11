import uuid
from datetime import datetime
import models


class BaseModel:
    """
    This class represents base model for all models in the application.
    """

    def __init__(self, *args, **kwargs):
        """Initialize BaseModel"""
        if kwargs:
            if 'id' in kwargs:
                self.id = kwargs['id']
            else:
                self.id = str(uuid.uuid4())
            if 'created_at' in kwargs:
                self.created_at = datetime.strptime(
                    kwargs['created_at'], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if 'updated_at' in kwargs:
                self.updated_at = datetime.strptime(
                    kwargs['updated_at'], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        """Return string representation of BaseModel"""
        attr_dict = {k: v for k, v in self.__dict__.items() if k not in ['id', 'created_at', 'updated_at']}
        return '[{}] ({}) {}'.format(type(self).__name__, self.id, attr_dict)

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
