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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ list to json"""

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps([obj.to_dictionary() for obj in list_dictionaries])

    @classmethod
    def save_to_file(cls, list_objs):
        """ object to json to file"""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="utf-8") as file:
            json_rep = cls.to_json_string(list_objs)
            file.write(json_rep)

    @staticmethod
    def from_json_string(json_string):
        """ from json rep to string"""

        if json_string is None:
            return ""
        return json.loads(json_string)
