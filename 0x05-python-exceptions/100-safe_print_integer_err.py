#!/usr/bin/python3

import sys

def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
    except Exception as err:
        sys.stderr.write("Exception: " + err.__str__() + "\n")
        return False
    else:
        return True
