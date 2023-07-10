#!/usr/bin/python3
"""Inherited class checking functions"""


def is_kind_of_class(obj, a_class):
    """Check if a class is an instance of a given class"""
    if isinstance(obj, a_class):
        return True
    return False
