#!/usr/bin/python3

def multiple_returns(sentence):
    """Check if sentence is valid"""
    if sentence == "":
        return (0, None)
    return (len(sentence), sentence[0])
