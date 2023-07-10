#!/usr/bin/python3
"""Class Checking"""


def is_same_class(obj, a_class):
    """Checks if a class is the same"""
    if type(obj) == a_class:
        return True
    return False
