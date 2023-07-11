#!/usr/bin/python3
"""Defines a python class student"""


class Student:
    """Class Student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student"""

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Get a dictionary representation"""
        return self.__dict__
