#!/usr/bin/python3
"""defines a fucntion that print my name"""


def say_my_name(first_name, last_name=""):
    """
    Args:
        -first_name (string): name
        -last_name (string): name
    """
    if not isinstance(first_name, str):
        raise TypeError('first_name must be a string')
    if not isinstance(last_name, str):
        raise TypeError('last_name must be a string')
    print("My name is {} {}".format(first_name, last_name))
