#!/usr/bin/python3
""" Write a class Student that defines a student """


class Student:
    """ this class creates a student"""

    def __init__(self, first_name, last_name, age):
        """ initaialises the class """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ return the dictionary rep """
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }
