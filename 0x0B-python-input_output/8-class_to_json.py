#!/usr/bin/python3
"""Defines a python class"""


def class_to_json(obj):
    """Returns a representation of a class"""
    return obj.__dict__
