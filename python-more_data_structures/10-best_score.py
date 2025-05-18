#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None

    best_key = None
    best_val = None
    for key, value in a_dictionary.items():
        if best_val is None or value > best_val:
            best_key = key
            best_val = value
    return best_key
