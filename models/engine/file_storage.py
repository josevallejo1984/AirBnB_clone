#!/usr/bin/python3
"""Serializes instances to a JSON file and.
   deserializes JSON file to instances
"""
import json


class FileStorage(object):
    """Define class FileStorage."""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return FileStorage.__objects

    def new(self, obj):
        key = obj.__class__.__name__ + '.' + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        new = {}
        with open(self.__file_path, mode='w', encoding='utf-8') as my_file:
            for k, v in FileStorage.__objects.items():
                new.update({k: v.to_dict()})
            my_file.write(json.dumps(new))

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as my_file:
                from models.base_model import BaseModel
                new_dict = json.loads(my_file.read())
                for k, v in new_dict.items():
                    objt = BaseModel(**v)
                    FileStorage.__objects[k] = objt

        except IOError:
            pass
