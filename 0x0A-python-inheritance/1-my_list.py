#!/usr/bin/python3
""" This module inherits from list """


class MyList(list):
    """ print a list """
    def print_sorted(self):
        print(sorted(self))
