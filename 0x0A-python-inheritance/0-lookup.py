#!/usr/bin/python3
""" This module looks up attribute and methods of an object"""


def lookup(obj):
    """
    This returns the methods and attributes
    of an object

    Args:
    obj: The Object

    Return:
    a list of the available attributes and methods
    """

    return list(dir(obj))
