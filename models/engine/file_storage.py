#!/usr/bin/python3
""" Serializes instances to a JSON file and 
deserializes JSON file to instances
"""
import models
from uuid import uuid4
from datetime import datetime
import json


class FileStorage(object):
    """Define class FileStorage"""
    def __init__(self):
        """Initialized constructor
        """
        self.__file_path = "file.json"
        self.__objects = {}
    
    def all(self):
        return self.__objects
    
    def new(self, obj):
        self.__objects.update({str(obj.__class__.__name__) + '.' + str(obj.id): obj.__dict__})

    def save(self):
        with open(self.__file_path, mode='w', encoding='utf-8') as my_file:
            my_file.write(json.dumps(self.__objects))

    def reload(self):
        try:
            with open(self.__file_path, mode='r', encoding='utf-8') as my_file:
                json.loads(my_file.read())
        except:
            pass

