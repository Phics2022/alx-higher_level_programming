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

    def area(self):
        """ returns tha area"""
        return self.__width * self.__height

    def __str__(self):
        """ return a string representation """
        string = "[{}] {}/{}"
        return string.format("Rectangle", self.__width, self.__height)
