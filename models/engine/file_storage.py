#!/usr/bin/python3

import json

class FileStorage:
    """FileStorage class

    This class manages the serialization and deserialization of objects to/from a JSON file.
    """

    def __init__(self):
        """Initialize FileStorage"""
        self.__file_path = 'file_path'
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
        json_str = json.dumps(self.__objects, default=lambda o: o.__dict__, indent=4)
        with open(self.__file_path, 'w') as file:
            file.write(json_str)

    def reload(self):
        """Deserializes the JSON file to __objects"""
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

