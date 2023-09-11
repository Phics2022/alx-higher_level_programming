#!/usr/bin/python3
""" A module that checks is an obj inherits from a class"""


def inherits_from(obj, a_class):
    """ Checks if obj inherits from a_class"""

    return issubclass(obj, a_class)
