#!/usr/bin/python3
"""
This module creates a rectangle class
which inherits from a class `Base`
"""
from base import Base


class Rectangle(Base):
    """ This is a rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """this is the class constructor"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """This the the width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        pass

    @property
    def height(self):
        """ This is the height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        pass

    @property
    def x(self):
        """ This is the `x` getter"""
        return self.__x

    @x.setter
    def x(self, value):
        pass

    @property
    def y(self):
        """This is the `y` getter"""
        return self.__y

    @y.setter
    def y(self, value):
        pass
