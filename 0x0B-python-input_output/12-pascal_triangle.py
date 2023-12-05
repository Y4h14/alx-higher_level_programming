#!/usr/bin/python3
"""define a pascal triangle"""


def pascal_triangle(n):
    """
    lists integers representing the Pascal’s triangle of n
    Args:
        -n (int): size of pascal triangle
    Return:
        an empty list if n <= 0
    """
    list = []
    if n <= 0:
        return list

