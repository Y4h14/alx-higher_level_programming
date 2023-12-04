#!/usr/bin/python3
"""define a rebel class"""


class MyInt(int):
    """a subclass of int"""
    def __eq__(self, other):
        """the equal function"""
        if int(self) == other:
            return False
        else:
            return True

    def __ne__(self, other):
        """not equal funciton"""
        if int(self) != other:
            return False
        else:
            return True
