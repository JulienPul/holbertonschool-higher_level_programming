#!/usr/bin/python3
"""
Module that defines MyList, a subclass of sorted list .
"""


class MyList(list):
    """subclass of sorted list"""
    def print_sorted(self):
        """
        Prints the list elements in ascending order.
        """
        print(sorted(self))
