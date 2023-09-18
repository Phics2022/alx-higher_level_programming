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

    def update(self, *args, **kwargs):
        """
        updates the argument
        for the *args
        1st argument should be the id attribute
        2nd argument should be the width attribute
        3rd argument should be the height attribute
        4th argument should be the x attribute
        5th argument should be the y attribute
        """

        if len(args) != 0:
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

    def to_dictionary(self):
        """ return the dictionaru representation of a square"""
        return {'id': self.id, 'size': self.size, 'x': self.x, 'y': self.y}
