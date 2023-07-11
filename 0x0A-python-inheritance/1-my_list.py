#!/usr/bin/python3
""" This module inherits from list """


class MyList(list):
    def print_sorted(self):
        print(sorted(self))
