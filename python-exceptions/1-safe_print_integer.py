#!/usr/bin/python3
def safe_print_integer(value):
    """
    print an integer value followed by a newline.
    Returns True if the value was successfully printed as an integer,
    False if a TypeError or ValueError occurred.
    """
    try:
        print("{:d}".format(value), end="")
        print()
        return True
    except (TypeError, ValueError):
        return False
