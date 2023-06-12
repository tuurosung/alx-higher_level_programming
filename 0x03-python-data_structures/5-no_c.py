#!/usr/bin/python3

def no_c(my_string):
    temp = [val for val in my_string if val != 'c' and val != 'C']
    return ("".join(temp))
