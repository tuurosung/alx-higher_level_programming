#!/usr/bin/python3
"""Define the base geo class"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Define the class of a rectangle extension of base geometry"""

    def __init__(self, width, height):
        """Initialize the class

        Args:
            width (init): the width of the rectangle
            height (init): the height of the rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
