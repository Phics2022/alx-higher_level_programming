#!/usr/bin/python3
""" this moduke checks if the obj is a kind """


def is_kind_of_class(obj, a_class):
    """ check is obj ia a kind of a_class
    Args:
    obj: object
    a_class: class

    Return:
    bool: True or False depending on the outcome
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
