#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """class of geometric shapes"""
    def area(self):
        """returns the area"""
        raise Exception('area() is not implemented')
