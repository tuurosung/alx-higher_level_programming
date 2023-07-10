#!/usr/bin/python3
"""Checks for instance"""

def inherits_from(obj, a_class):
    """Checks for instance"""
    if issubclass(type(obj), a_class) and type(obj) != a_class:
        return True
    return False
