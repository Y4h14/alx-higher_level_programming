#!/usr/bin/python3
"""define a fucntion that check if object is instance of class"""


def inherits_from(obj, a_class):
    """
        check if an object is of a class or subclass
        Args:
            -obj: object
            -a_class: a class
        Return:
            True if the object is instance of a class that
            inherited from the specifed class,
            otherwise False.
    """
    return (issubclass(type(obj), a_class) and type(obj) != a_class)
