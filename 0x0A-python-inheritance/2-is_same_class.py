#!/usr/bin/python3
"""
Write a function that returns True if the object
s exactly an instance of the specified class ;
otherwise False.
"""


def is_same_class(obj, a_class):
    """
    checks if an object is an instance of a class

    Args:
    obj: The object to check
    a_class: The class 

    Return:
    True(Bool): if obj is an instance of a_class
    False(Bool): if obj is not an instance of a_class
    """

    if isinstance(obj, a_class):
        return type(obj) == a_class
