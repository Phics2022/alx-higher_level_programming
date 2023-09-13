#!/usr/bin/python3
"""student to json"""


class Student:
    """ a student class"""

    def __init__(self, first_name, last_name, age):
        """ initialise the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieves the dictionary rep of instance"""

        if attrs is None:
            serialised = {
                    'first_name': self.first_name,
                    'last_name': self.last_name,
                    'age': self.age}
            return serialised
        else:
            serialised = {}
            for attr in attrs:
                if hasattr(self, attr):
                    serialised[attr] = getattr(self, attr)
                else:
                    continue
            return serialised

    def reload_from_json(self, json):
        """ replace all attributes"""
        for key, value in json.items():
            if hasattr(self, key):
                setattr(self, key, value)
