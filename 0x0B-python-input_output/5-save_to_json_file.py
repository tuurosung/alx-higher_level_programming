#!/usr/bin/python3
"""A function for encoding string to json"""
import json


def save_to_json_file(my_obj, filename):
    """Write an object to a file"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
