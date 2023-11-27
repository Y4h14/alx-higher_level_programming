#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """ defines a rectangle object"""

    def __init__(self, width=0, hieght=0):
        """
        intiate a rectangle instant
        Args:
            -width (int): the width of the rectangle
            -height (int): the height of the rectangle
        """
        self.width = width
        self.height = hieght

    @property
    def width(self):
        """return the value of width"""
        return self.__width

    @property
    def hieght(self):
        """return the value of hieght"""
        return self.hieght

    @width.setter
    def width(self, value):
        """sets the width values"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @hieght.setter
    def height(self, value):
        """sets the height values"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))
