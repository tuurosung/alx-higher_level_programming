#!/usr/bin/python3

def simple_delete(a_dictionary):
    dup = {}
    for key, value in a_dictionary.items():
        dup.update({key: (value * 2)})
    return dup
