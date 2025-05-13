#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    """
    Return new list with elements multiplied by number with map
    """
    return list(map(lambda x: x * number , my_list))
