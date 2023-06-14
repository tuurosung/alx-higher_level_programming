#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    dict_keys = list(a_dictionary.keys())
    dict_keys.sort()
    for dict_key in dict_keys:
        print("{}: {}".format(dict_key, a_dictionary[dict_key]))
