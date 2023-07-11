#!/usr/bin/python3
"""Defines a python class student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student"""


    def to_json(self):
        """Get a dictionary representation"""
        return self.__dict__
