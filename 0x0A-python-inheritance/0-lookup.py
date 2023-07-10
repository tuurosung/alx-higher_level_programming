#!/usr/bin/python3
"""A function that returns a list of available attributes"""


def lookup(obj):
    """ Returns the list of available attributes """
    return (dir(obj))
