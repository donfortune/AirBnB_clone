#!/usr/bin/python3

import json
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class

    This class manages the serialization and deserialization of objects to/from a JSON file.
    """

    def __init__(self):
        """Initialize FileStorage"""
        self.__file_path = 'file.json'  # Correct the file path
        self.__objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(type(obj).__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        json_dict = {}
        for key, obj in self.__objects.items():
            json_dict[key] = obj.to_dict()  # Serialize each object to a dictionary
        with open(self.__file_path, 'w') as file:
            json.dump(json_dict, file, indent=4)  # Dump the dictionary to JSON

    def reload(self):
        """reloads"""
        try:
            with open(self.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    module = __import__('models.' + class_name, fromlist=[class_name])
                    cls = getattr(module, class_name)
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass

