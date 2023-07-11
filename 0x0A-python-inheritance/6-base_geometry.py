#!/usr/bin/python3
""" creates a geometry"""


class BaseGeometry:
    """create a base geometry"""

    def area(self):
        """ raise area exception"""
        raise Exception("area() is not implemented")
