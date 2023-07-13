#!/usr/bin/python3
""" this module appends a text to a file"""


def append_write(filename="", text=""):
    """appends `text` to a file `filename`"""
    with open(filename, 'a', encoding="utf-8") as f:
        byte_appended = f.write(text)
        return byte_appended
