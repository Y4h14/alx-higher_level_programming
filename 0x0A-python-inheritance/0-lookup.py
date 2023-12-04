#!/usr/bin/python3
"""defines a method that returns the attributes and methods of an object"""


def lookup(obj):
    """
    Args:
        - obj (object): the object to look up
    """
    return dir(obj)
