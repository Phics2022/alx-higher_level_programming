#!/usr/bin/python3
"""This module contains the add function"""


def add_integer(a, b=98):
    """This function adds two integers
    Args:
    a(int): parameter
    b(int): parameter

    Return:
    int: a + b

    Raise:
    TypeError: if a or b is not int or float
    """
    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (float, int)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
