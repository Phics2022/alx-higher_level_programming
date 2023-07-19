#!/usr/bin/python3
""" This module creates a sqaure class"""


from models.rectangle import Rectangle
from models.base import Base


class Square(Rectangle):
    """ a Square class that inherits from
    Rectangle class
    """

    def __init__(self, size, x=0, y=0, id=None):
        """ Initialises the class """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ the string method"""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ returns the width and height"""
        return self.width

    @size.setter
    def size(self, value):
        super().__init__(value, value)

    def update(self, *args, **kwargs):
        """ updates the square"""
        if len(args) > 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
                self.height = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.width = value
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value
