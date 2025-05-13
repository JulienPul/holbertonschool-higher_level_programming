#!/usr/bin/puthon3
def update_dictionary(a_dictionary, key, value):
    """
    Updates a_dictionary by setting a_dictionary[key] = value,
    replacing any existing value or adding a new key if not present.
    Returns the modified dictionary.
    """
    a_dictionary[key] = value
    return a_dictionary
