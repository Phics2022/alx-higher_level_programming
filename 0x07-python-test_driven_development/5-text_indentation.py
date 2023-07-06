#!/usr/bin/python3
""" this moddule does text indentation """


def text_indentation(text):
    """ text indentation module
    Args:
    text(str): string

    Raise:
    TypeError: when text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    ind = [".", "?", ":"]
    lines = text.splitlines()
    for x, line in enumerate(lines):
        line = line.strip()
        line = line.replace(". ", ".")
        line = line.replace("? ", "?")
        line = line.replace(": ", ":")
        for char in ind:
            line = line.replace(char, char + "\n\n")

        print(line, end="")
