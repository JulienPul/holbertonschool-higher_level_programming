#!/usr/bin/python3
"""
Module 1-rectangle:
Defines a class Rectangle with width and height.
"""


class Rectangle:
    """Define a rectangle by width and height."""

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): width of the rectangle sides (default 0)
            height (int): height of the rectangle sides (default 0)
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height ensuring it's a non-negative integer."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
