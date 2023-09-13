#!/usr/bin/python3
""" This module converts string to json"""


import json


def to_json_string(my_obj):
    """ change `my_obj` to json"""

    return json.dumps(my_obj)
