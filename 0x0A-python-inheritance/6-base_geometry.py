#!/usr/bin/python3
""" This module creates a geometry class"""


class BaseGeometry:
    """ This is a base geometry class"""

    def area(self):
        """ raises an exception"""
        raise Exception("area() is not implemented")
