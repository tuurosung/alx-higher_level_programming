#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """Duplicate list"""
    list = my_list
    """check if idx is valid in list"""
    if idx < 0 or idx > (len(my_list) - 1):
        return list

    else:
        my_list[idx] = element
        return my_list
