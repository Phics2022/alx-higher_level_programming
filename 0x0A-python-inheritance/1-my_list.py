#!/usr/bin/python3
""" This module creates a function that inherits from list"""


class MyList(list):
    """ This class inherits from lists"""

    def print_sorted(self):
        """ this function prints a sorted list"""
        sorted_list = sorted(self)
        print(sorted_list)
