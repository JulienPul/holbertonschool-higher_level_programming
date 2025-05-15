#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    """
    Print x integers from my_list, one per element on the same line,
    followed by a new line. Skip non-integer elements.
    Return the number of integers printed.
    """

    
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (IndexError):
            break
        except (TypeError, ValueError):
            continue
    print()
    return count
