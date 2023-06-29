#!/usr/bin/python3
"""This module creates a class Squares with some abilities"""


class Square:
    """This class creates a square"""
    def __init__(self, size=0, position=(0, 0)):
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
            self.__position = position

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

    @property
    def position(self):
        """ tuple: gets the position """
        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ computes the area of the size
        Return:
            int: the square
        """
        return self.__size * self.__size

    def my_print(self):
        """ prints a square"""
        if self.__size == 0:
            print()
        else:
            for x in range(self.size):
                for z in range(self.position[0]):
                    print(" ", end="")
                for y in range(self.size):
                    print("#", end="")
                print()
