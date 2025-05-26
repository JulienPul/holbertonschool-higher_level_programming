#!/usr/bin/python3
"""
Module that defines MyList, a subclass of sorted list .
"""


class MyList(list):
    """
        Prints the list elements in ascending order.
        """
    def print_sorted(self):
        print(sorted(self))
