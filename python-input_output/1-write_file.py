#!/usr/bin/python3
"""
Write a function that writes a string to a text file (UTF8)
and returns the number of characters.
"""


def write_file(filename="", text=""):
    """ module write_file
    """
    with open(filename, 'w') as f:
        return f.write(text)
