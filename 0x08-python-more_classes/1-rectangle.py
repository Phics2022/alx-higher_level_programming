#!/usr/bin/python3
""" This module creates a Rectangle class """


class Rectangle():
    """ This is a rectangle class"""
    def __init__(self, width=0, height=0):
        """ This initialises an instance"""
        if not isinstance(width, int):
            raise TypeError("width must be an integer")
        elif width < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = width
        if not isinstance(height, int):
            raise TypeError("height must be an integer")
        elif height < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = height
    # the width and height getter and setter

    @property
    def width(self):
        """ returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise TypeError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ returns the height"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise TypeError("height must be >= 0")
        else:
            self.__height = value
