#!/usr/bin/python3
""" creates a rectangle class"""


from models.base import Base


class Rectangle(Base):
    """ creates a rectangle object
    and it inherits from Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ initailises the class"""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """returns the width"""
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        """returns the width"""
        return self.__height

    @width.setter
    def width(self, value):
        self.__height = value

    @property
    def x(self):
        """returns the width"""
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    @property
    def y(self):
        """returns the width"""
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
