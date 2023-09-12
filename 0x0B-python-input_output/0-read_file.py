#!/usr/bin/python3
""" This module creates a function that reads a file"""


def read_file(filename=""):
    """ This function reads a file and prints it's content"""
    with open(filename, "r", encoding="utf-8") as file:
        buff = file.read()
        print(buff, end="")
