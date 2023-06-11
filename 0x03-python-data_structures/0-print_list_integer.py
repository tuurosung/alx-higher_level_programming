#!/usr/bin/python3

"""Define the function"""
def print_list_integer(my_list=[]):

    """Loop through the list of integers"""
    for i in range(len(my_list)):
        print("{:d}".format(my_list[i]))
