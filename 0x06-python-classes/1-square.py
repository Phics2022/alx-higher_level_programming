#!/usr/bin/python3
"""This module creates a class Squares with some abilities"""


class Square:
    """This class creates a square"""
    def __init__(self, size):
        """ initialise the size of the square
        Args:
            size (int): size of the square
        """
        self.__size = size
