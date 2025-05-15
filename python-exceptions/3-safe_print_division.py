#!/usr/bin/python3
def safe_print_division(a, b):
    """
    Divide two integers and print the result.
    Returns: result of division, or None if an error occurred.
    Uses try/except/finally
    """

    inside_result = None
    try:
        inside_result = a / b
    except (ZeroDivisionError):
        inside_result = None
    finally:
        print("Inside result: {}".format(inside_result))
    return inside_result
