#!/usr/bin/python3
""" This module converts json to object"""


import json


def from_json_string(my_str):
    """ This function converts `my_str` from json to object"""

    return json.loads(my_str)
