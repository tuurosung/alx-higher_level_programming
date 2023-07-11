#!/usr/bin/python3
"""A function for reading a file"""
import json


def load_from_json(filename):
    """Create a new oobject from a json file"""
    with open(filename) as f:
        return json.load(f)
