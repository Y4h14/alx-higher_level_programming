#!/usr/bin/python3
"""define a function that check if an object is an instance
    of a specific class
"""


def is_same_class(obj, a_class):
    """
    Args:
        -obj : the object to check
        -a_class: the class to check
    """
    return isinstance(obj, a_class) and type(obj) is a_class
