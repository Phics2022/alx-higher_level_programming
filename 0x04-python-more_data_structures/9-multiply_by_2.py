#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = {}
    for y, i in a_dictionary.items():
        new_dict[y] = i * 2
    return new_dict
