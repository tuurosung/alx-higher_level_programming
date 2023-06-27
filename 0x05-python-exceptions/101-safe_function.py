#!/usr/bin/python3
import sys

def safe_function(fct, *args):
    result = None

    try:
        resutl = fct(*args)

    except Exception as err:
        sys.stderr.write("Exception: " + err.__str__() + "\n")
        return None

    else:
        return result
