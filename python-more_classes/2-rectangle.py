#!/usr/bin/python3
"""Module 2-rectangle:
define a rectangle perimeter and area"""


class Rectangle:
    def __init__(self, width=0, height=0):
        """define a rectangle with height and width
        """
        self.height = height
        self.width = width

    @property
    def height(self):
        """height to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """set value to height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """width to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """set value to width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """retrieve the area"""
        return self.__height * self.__width

    def perimeter(self):
        """retrieve perimeter"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return (self.__width + self.__height) * 2
