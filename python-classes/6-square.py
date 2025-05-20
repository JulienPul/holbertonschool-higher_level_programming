#!/usr/bin/python3
"""
Module 6-square:
define a class square with size and position
"""


class Square:
    """define a square with size and position"""

    def __init__(self, size=0, position=(0, 0)):
        """Private instance attribute: size:
        property def size(self): to retrieve it
        property setter def size(self, value):
        size must be an integer, otherwise raise a TypeError exception
          with the message size must be an integer
        if size is less than 0, raise a ValueError exception
          with the message size must be >= 0
        Private instance attribute: position:
        property def position(self): to retrieve it
        property setter def position(self, value): to set it:
        position must be a tuple of 2 positive integers,
        otherwise raise a TypeError exception with
        the message position must be a tuple of 2 positive integers
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square"""
        return self.__size

    @size.setter
    def size(self, value):
        """Define size of the side with validation"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """define the position to retrieve it"""
        return self.__position

    @position.setter
    def position(self, value):
        """position is a tuple of 2 positive integers."""
        if (
            not isinstance(value, tuple) or
            len(value) != 2 or
            not all((isinstance(num, int) and num >= 0) for num in value)
        ):
            raise TypeError(
                "position must be a tuple of 2 positive integers"
                )
        self.__position = value

    def area(self):
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print()
            return
        for _ in range(self.__position[1]):
            print()
        for _ in range(self.__size):
            print(' ' * self.__position[0] + '#' * self.__size)
