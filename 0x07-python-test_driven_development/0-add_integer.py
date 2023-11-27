#!/usr/bin/python3
""" has a function that adds two integers"""


def add_integer(a, b=98):
    """
    adds two integers

    Args:
        -a (int or float): the first number
        -b (int or float): the seconde number
    """
    if type(a) is not int:
        if type(a) is not float:
            raise TypeError('a must be an integer')
    if type(b) is not int:
        if type(a) is not float:
            raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return (a + b)        
