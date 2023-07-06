#!/usr/bin/python3
""" This module prints out your name"""


def say_my_name(first_name, last_name=""):
    """ prints out your name
    Args:
    first_name(string): your first name
    last_name(string): your last name
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")