#!/usr/bin/python3
""" this module returns the json rep of an object"""


import json


def to_json_string(my_obj):
    """ turn`my_obj` to a json representation"""
    x = json.dumps(my_obj)
    return x
