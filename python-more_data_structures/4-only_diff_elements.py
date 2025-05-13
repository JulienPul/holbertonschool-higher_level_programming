#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Return a set of elements that are present in only one of set_1 or set_2.
    """
    return set_1 ^ set_2
