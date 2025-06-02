#!/usr/bin/python3
"""module 3-jsonstring"""
import json


def to_json_string(my_obj):
    """ function that returns the JSON
    representation of an object (string):"""
    json_string = json.dumps(my_obj)
    return json_string
