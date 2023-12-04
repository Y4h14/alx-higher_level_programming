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
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
