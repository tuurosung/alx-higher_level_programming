#!/usr/bin/python3
"""A function that counts the number of lines in a file"""


def number_of_lines(filename=""):
    """Returns the number of lines in the given file"""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
