#!/usr/bin/python3
"""mudule 2:Converting CSV Data to JSON Format"""
import csv
import json


def convert_csv_to_json(filename):
    """takes the CSV filename as its parameter """
    try:
        with open(filename, 'r') as csv_file:
            reader = csv.DictReader(csv_file)
            data = list(reader)

        with open(filename, 'w') as json_file:
            json.dump(data, json_file)
        return True

    except FileNotFoundError:
        return False
