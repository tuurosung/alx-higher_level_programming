#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    res = None

    try:
        res = fct(*args)

    except Exception as err:
        sys.stderr.write("Exception: " + err.__str__() + "\n")
        return None

    else:
        return res
