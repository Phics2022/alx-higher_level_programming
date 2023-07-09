#!/usr/bin/python3
""" This module creates an empty class"""


class Rectangle:
    """ create an empty class"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
            rec += str(self.print_symbol) * self.__width + "\n"
        rec += str(self.print_symbol) * self.__width
        return rec

    def __repr__(self):
        """ create a formal representation"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """ delete an object"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """ compare rectangles
        Args:
        rect1: instance 1
        rect2: instance 2

        Return:
        the biggest rectangle based on the area
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """ create a square instance of a class
        Args:
        cls: the class
        size: the size
        """
        return cls(size, size)
