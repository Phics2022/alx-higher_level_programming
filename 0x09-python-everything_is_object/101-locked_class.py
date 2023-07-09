#!/usr/bin/python3
""" creates a locked class """


class LockedClass:
    """ creates a locked class with only first name
    allowed """
    __slots__ = ('first_name',)
