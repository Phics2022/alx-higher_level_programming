#!/usr/bin/python3
""" this module writes to a file"""


def write_file(filename="", text=""):
    """write text into a file `filename`
    Args:
    filename(string): file name
    text: content to write
    """
    with open(filename, 'w', encoding="utf-8"):
        f.write(text)
