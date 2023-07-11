#!/usr/bin/python3
"""A function that appends a string to a file"""


def write_file(filename="", text=""):
    """Appends a string to a file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
