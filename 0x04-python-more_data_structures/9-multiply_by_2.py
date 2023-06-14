#!/usr/bin/python3

def multipy_by_2(a_dictionary):
    dup = {}
    for key, value in a_dictionary.items():
        dup.update({key: (value * 2)})
    return dup
