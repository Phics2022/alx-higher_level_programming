#!/usr/bin/python3
""" This module appends to a file"""


def append_write(filename="", text=""):
    """This funvction appends `text` to `filename`"""

    with open(filename, "a", encoding="utf-8") as file:
        length = file.write(text)
    return length
