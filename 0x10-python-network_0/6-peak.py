#!/usr/bin/python3
"""defines a fucntion the calculates the peak"""


def find_peak(list_of_integers):
    """takes a list and finds the peak"""
    if list_of_integers is None or len(list_of_integers) == 0:
        return None

    list_of_integers.sort()
    return list_of_integers[-1]
