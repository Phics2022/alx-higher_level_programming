#!/usr/bin/python3
"""This module creates a class Squares with some abilities"""


class Square:
    """This class creates a square"""
    def __init__(self, size=0):
        """ initialise the size of the square
        Args:
            size: size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    @property
    def size(self):
        """ int: gets the size of the square """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ computes the area of the size
        Return:
            int: the square
        """
        return self.__size * self.__size
