#!/usr/bin/python3
""" This module writes to a file"""


def write_file(filename="", text=""):
    """ This function writes `text` to `filename`"""

    with open(filename, "w", encoding="utf-8") as file:
        lent = file.write(text)
    return lent
