#!/usr/bin/python3
"""
This is module creates a square class that
inherits from the Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """ This is a square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """ This is the class constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """the string representation"""
        print_out = "[Square] ({}) {}/{} - {}"
        return print_out.format(self.id, self.x, self.y, self.width)

    @property
    def size(self):
        """ This returns the size"""
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value
