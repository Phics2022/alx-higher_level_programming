#!/usr/bin/python3
""" from json to object """


import json


def from_json_string(my_str):
    """ turn `my_str` to an object
    Args:
    my_str
    """
    x = json.loads(my_str)
    return x
