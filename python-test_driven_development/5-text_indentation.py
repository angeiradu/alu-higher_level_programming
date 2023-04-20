#!/usr/bin/python3
"""Defines a text-indentation function."""


def text_indentation(text):
    """Print text with two new lines after each '.', '?', and ':'.
    Args:
        text (string): The text to print.
    Raises:
        TypeError: If text is not a string.
        """
        if type(text) != str:
        raise TypeError('text must be a string')
    for char in text:
        if char == '.' or char == '?' or char == ':':
            print(char, '\n\n')
        else:
            print(char, end='')
