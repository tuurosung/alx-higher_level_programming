#!/usr/bin/python3

def best_score(a_dictionary):
    """Check if a dictionary"""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    s_list = list(a_dictionary.keys())[0]
    max = a_dictionary[s_list]
    for x, y in a_dictionary.items():
        if y > max:
            max = y
            s_list = x
    return (s_list)
