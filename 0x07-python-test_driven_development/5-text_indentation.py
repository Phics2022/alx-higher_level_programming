#!/usr/bin/python3
""" This module is a text indentation one"""


def text_indentation(text):
    cp = text
    """This is the text indentation function"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for x, i in enumerate(text):
        if text[x - 1] == "." or text[x - 1] == ":":
            continue
        if text[x - 1] == "?":
            continue
        print(i, end="")
        if i == "." or i == "?" or i == ":":
            print("\n")

