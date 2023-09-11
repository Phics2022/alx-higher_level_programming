#!/usr/bin/python3
""" This module creates a square class"""


Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """ This is a square class inheritting from Rectangle class"""

    def __init__(self, size):
        """ This initialises the class with size """
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """ returns the area """
        return self.__size * self.__size

    def __str__(self):
        string = "[Square] {}/{}"
        return string.format(self.__size, self.__size)
