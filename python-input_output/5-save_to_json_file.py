#!/usr/bin/python3
"""module 5-save object to a file"""
import json


def save_to_json_file(my_obj, filename):
    """function that writes an Object to a text file
    , using a JSON representation:"""
    with open(filename, "w") as f:
        f.write(json.dumps(my_obj))
