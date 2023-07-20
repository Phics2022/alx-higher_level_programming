#!/usr/bin/python3
""" this module creates a base class """

import json


class Base:
    """ The base module class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialises the class """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation"""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
