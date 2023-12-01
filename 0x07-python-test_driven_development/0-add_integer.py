#!/usr/bin/python3
""" has a function that adds two integers"""


def add_integer(a, b=98):
    """
    adds two integers

    Args:
        -a (int or float): the first number
        -b (int or float): the seconde number
    """
    if not isinstance(a, int):
        if isinstance(a, float):
            a = int(a)
        else:
            raise TypeError("a must be an integer")
    if not isinstance(b, int):
        if isinstance(b, float):
            b = int(b)
        else:
            raise TypeError("b must be an integer")
    return a + b
