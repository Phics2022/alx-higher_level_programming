#!/usr/bin/python3
""" write an object to a file the JSON way"""


import json


def save_to_json_file(my_obj, filename):
    """ use json to write `my_obj` to `filename` """
    with open(filename, 'a', encoding="utf-8") as f:
        json.dump(my_obj, f)
