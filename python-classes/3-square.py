#!/usr/bin/python3
"""
Module 3-square:
 defines a square by: area method(based on 2-square.py)
"""


class Square:
    """
    Define a square with lenght side"""

    def __init__(self, size=0):
        """Square instance with size validation
        size must be an integer, otherwise raise a TypeError exception
         size must be an integer
        if size is less than 0, raise a ValueError exception
         size must be >= 0
        Public instance method: def area(self):returns the current square area
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return self.__size ** 2
