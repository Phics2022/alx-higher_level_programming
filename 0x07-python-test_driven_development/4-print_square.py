#!/usr/bin/python3
""" this module prints a square of # characters """


def print_square(size):
    """ Print a square of size `size`
    Args:
    size(int): size of the square

    Raise:
    TypeError: when size id less then zero or is not an integer

    """
    if not isinstance(size, (int, float)):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    for i in range(int(size)):
        for x in range(int(size)):
            print("#", end="")
        print()
