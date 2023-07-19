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
