#!/usr/bin/python3
""" This module print a square"""


def print_square(size):
    """ This module prints a square"""

    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    size = int(size)
    for i in range(size):
        for j in range(size):
            print("#", end="")
        print()
