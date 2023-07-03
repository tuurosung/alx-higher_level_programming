#!/usr/bin/python3
"""A class that defines the rectangle class"""


class Rectangle:
    """Defines the rectangle class"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initializes the rectangle
        Args:
                width (int): width of the rectangle
                height (int): height of the rectangle
        """
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    @property
    def width(self):
        """The width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """The height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Returns representation of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return ("")

        r = []
        for i in range(self.__height):
            [r.append('#') for j in range(self.__width)]
            if i != self.__height - 1:
                r.append("\n")
        return ("".join(r))

    def __repr__(self):
        """Returns a string representation of rectangle"""
        r = "Rectangle(" + str(self.__width)
        r += ", " + str(self.__height) + ")"
        return (r)

    def __del__(self):
        """Deletes rectangle"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
