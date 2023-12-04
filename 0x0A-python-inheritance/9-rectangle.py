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


class Rectangle(BaseGeometry):
    """a rectangle class"""

    def __init__(self, width, height):
        """an init fucntion"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """calculates the area of a rectangle"""
        return (self.__width * self.__height)

    def __str__(self):
        result = f"[Rectangle] {self.__width}/{self.__height}"
        return result
