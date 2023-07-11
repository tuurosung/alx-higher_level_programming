#!/usr/bin/python3
"""Define the base geo class"""


def add_attribute(obj, att, value):
    """Add a new attribute

    Args:
        obj (any): The object to add
        att (str): The name of the attribute
        value (any): The value of the attribute
    Raises:
        TypeError: If the attribute is not added
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, att, value)
