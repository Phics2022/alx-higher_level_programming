#!/usr/bin/python3
""" This module creates an empty class"""


class Rectangle:
    """ create an empty class"""
    def __init__(self, width=0, height=0):
        """ initialises the object

        Args:
        width(int): width of the rectangle
        height(int): height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """ int: gets the value of width """
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """int: gets the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ returns the area """
        return self.__width * self.__height

    def perimeter(self):
        """ returns the perimeter """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ print the # format of the string """
        if self.__width == 0 or self.__height == 0:
            return ""
        rec = ""
        for i in range(self.__height - 1):
            rec += "#" * self.__width + "\n"
        rec += "#" * self.__width
        return rec

    def __repr__(self):
        """ create a formal representation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ delete an object"""
        print("Bye rectangle...")
