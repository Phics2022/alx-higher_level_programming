#!/usr/bin/python3
""" This module loads json from file"""
import json


def load_from_json_file(filename):
    """ create abject from `filename`"""

    with open(filename, "r", encoding="utf-8") as file:
        buff = json.load(file)
    return buff
