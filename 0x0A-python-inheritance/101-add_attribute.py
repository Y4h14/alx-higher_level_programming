#!/usr/bin/python3
"""define a fucntion that adds attributes"""


def add_attribute(obj, name, value):
    """
    adds an attribute to an object
    Args:
        -obj: the object
        -name: the attribute name
        -value: the attribute name
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
