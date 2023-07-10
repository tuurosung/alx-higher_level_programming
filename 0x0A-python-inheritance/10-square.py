#!/usr/bin/python3
"""Define the base geo class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Define a square class"""
    def __init__(self, size):
        """Initialize a square class
        Args:
                size (int): size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
