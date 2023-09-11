#!/usr/bin/python3
""" This module creates a rectangle class"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Creates a rectangle class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """ initialises the class with wisth and height"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
