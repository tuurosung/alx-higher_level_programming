#!/usr/bin/python3

def search_replace(my_list, search, replace):

    """create new copy of my list"""
    dup = my_list[:]

    for i in range(len(dup)):
        if dup[i] == search:
            dup[i] = replace

    return (dup)
