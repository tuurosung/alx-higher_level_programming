#!/usr/bin/python3
"""A Class that inherits a class"""


class MyList(list):
    """Define a public instance method """
    def __init__(self):
        """initialize"""
        super().__init__()

    def print_sorted(self):
        """Print a sorted list """
        print(sorted(self))