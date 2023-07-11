#!/usr/bin/python3
""" this module check for subclasses"""


def inherits_from(obj, a_class):
    """ check if an object is ..."""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    else:
        return False
