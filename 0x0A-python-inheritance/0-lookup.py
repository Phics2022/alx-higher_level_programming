#!/usr/bin/python3
""" Attributes and methods """


def lookup(obj):
    """ gets the methods and attributes of an object
    Args:
    obj(object): the object to check out

    Return:
    A list of the objects and attributes
    """
    attr = dir(obj)
    lister = [i for i in attr]
    return lister
