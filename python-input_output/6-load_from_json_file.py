#!/usr/bin/python3
"""create object from json file"""
import json


def load_from_json_file(filename):
    """ function that creates an Object from a “JSON file”:"""
    with open(filename, "r") as f:
        return json.load(f)
