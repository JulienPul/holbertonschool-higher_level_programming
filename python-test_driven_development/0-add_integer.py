#!/usr/bin/python3
"""
0-add_integer module.

This module provides one function, add_integer() to add two numbers.
"""

def add_integer(a, b=98):
    """
    Add two integers.

    Returns the sum of a and b.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
