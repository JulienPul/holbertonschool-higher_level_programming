#!/usr/bin/python3
"""Module 11-square"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """class square"""
    def __init__(self, size):
        """Instantiation with size"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Return the area of the square."""
        return self.__size * self.__size

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
