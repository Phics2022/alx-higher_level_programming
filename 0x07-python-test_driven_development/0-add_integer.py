#!/usr/bin/python3
""" This module does additional calculation"""


def add_integer(a, b=98):
    """ this function adds a to b"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
