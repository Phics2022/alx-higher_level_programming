#!/usr/bin/python3
""" is it an instance """


def is_same_class(obj, a_class):
    """ checks if an object is an instance of a class
    Args:
    obj: The object to check
    a_class: the class to check

    Return:
    bool: True or False depending on the anser
    """
    if type(obj) == a_class:
        return True
    else:
        return False
