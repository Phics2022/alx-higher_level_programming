#!/usr/bin/python3
""" This creates a base class"""
import json


class Base:
    """ This is a base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """ This is the class constructor"""

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ list to json"""

        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)
