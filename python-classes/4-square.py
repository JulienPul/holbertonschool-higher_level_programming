#!/usr/bin/python3
"""
Module 4-square:
Define a class square with area method
"""


class Square:
    """define a square with thelenght of side"""
    def __init__(self, size=0):
        """Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value): to set it:
        size must be an integer, otherwise raise a TypeError exception
        with the message size must be an integer
        if size is less than 0, raise a ValueError exception
        with the message size must be >= 0
        """
        self.size = size
    @property
    def size(self):
        """ property def size(self): to retrieve it"""
        return self.__size

    @size.setter
    def size(self, value):
        """define size of the side with validation"""

        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return square area"""
        return self.__size ** 2
