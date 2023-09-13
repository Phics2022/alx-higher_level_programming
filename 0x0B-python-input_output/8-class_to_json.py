#!/usr/bin/python3
"""
this module creates the dictionary description of
an object for json serialisatoin
"""


def class_to_json(obj):
    """
    returns the dictionary description with
    simple data structure
    """

    if isinstance(obj, dict):
        return obj

    if hasattr(obj, "__dict__"):
        serialised = {}
        for key, value in obj.__dict__.items():
            if isinstance(value, (int, str, bool, list, dict)):
                serialised[key] = value
            elif isinstance(value, object):
                serialised[key] = class_to_json(value)
        return serialised_
