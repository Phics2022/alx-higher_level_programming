#!/usr/bin/python3
""" this module  returns the dictionary
description with simple data structure
"""


def class_to_json(obj):
    """  returns the dictionary
    description with simple data structure
    """
    json_dict = {}
    attribute_items = obj.__dict__

    for attr, value in attribute_tems.items():
        if isinstance(value, (list, dict, str, int, bool)):
            json_dict[attr] = value

    return json_dict
