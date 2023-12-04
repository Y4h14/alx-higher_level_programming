#!/usr/bin/python
"""define an extended verison of list"""


class MYList(list):
    """an extention to list type"""
    def print_sorted(self):
        """print a sorted object"""
        copy = self[:]
        copy.sort()
        print(copy)
