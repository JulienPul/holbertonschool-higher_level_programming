#!/usr/bin/python3
"""Module 7: Integer validator"""


class BaseGeometry:
    """class BaseGeometry (based on 6-base_geometry.py)."""

    def area(self):
        """Raise an Exception for unimplemented area()."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate that 'value' is a positive integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
