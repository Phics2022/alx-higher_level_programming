#!/usr/bin/python3
"""student to json"""


class Student:
    """ a student class"""

    def __init__(self, first_name, last_name, age):
        """ initialise the class"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves the dictionary rep of instance"""

        serialised = {
                'first_name': self.first_name,
                'last_name': self.last_name,
                'age': self.age}
        return serialised
