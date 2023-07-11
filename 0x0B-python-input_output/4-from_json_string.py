#!/usr/bin/python3
"""A function for encoding string to json"""
import json


def from_json_string(my_str):
    """Decodes a json to a string"""
    return json.loads(my_str)
