#!/usr/bin/python3
"""
    define a function that check f the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class
"""


def is_same_class(obj, a_class):
    """
    Args:
        -obj : the object to check
        -a_class: the class to check
    """
    return isinstance(obj, a_class) or is subclass(type(obj), a_class)
