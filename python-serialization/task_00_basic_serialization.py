#!/usr/bin/python3
"""0. Basic Serialization"""
import json


def serialize_and_save_to_file(data, filename):
    """Serialize a dictionary and save it to a JSON file."""
    with open(filename, "w") as f:
        json.dump(data, f)

def load_and_deserialize(filename):
    """Load data from a JSON file and
    deserialize it into a Python dictionary."""
    with open(filename, "r") as f:
        json.load(f)
