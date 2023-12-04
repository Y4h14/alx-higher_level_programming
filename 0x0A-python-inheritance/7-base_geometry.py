#!/usr/bin/python3
"""defines a class BaseGeometry"""


class BaseGeometry:
    """class of geometric shapes"""
    def area(self):
        """returns the area"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """
        validate value
        Args:
            -name (str): a string for a name
            -value (int): the value
        """
        if not isinstance(value, int):
            raise TypeError(name + ' must be an integer')
        if value <= 0:
            raise ValueError(name + ' must be greater than 0')
