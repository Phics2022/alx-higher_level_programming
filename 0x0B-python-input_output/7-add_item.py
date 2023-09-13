#!/usr/bin/python3
""" adds all argument to a python list"""
from sys import argv
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file


buff = argv[1:]
filename = "add_item.json"
save(buff, filename)
bluff = load(filename)
