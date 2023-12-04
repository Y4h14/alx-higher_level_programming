#!/usr/bin/pyhton3
"""defines a child class for class list"""


class MyList(list):
    """child class of the list class"""
    def print_sorted(self):
        """print list but sorted"""
        print(sorted(self))
