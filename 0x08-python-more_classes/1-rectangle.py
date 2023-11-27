#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """ defines a rectangle object"""

    def __init__(self, width=0, height=0):
        """
        intiate a rectangle instant
        Args:
            -width (int): the width of the rectangle
            -height (int): the height of the rectangle
        """
        if not isinstance(width, int):
            raise TypeError('width must be an integer')
        if width < 0:
            raise ValueError('width must be >= 0')
        self.__width = width

        if not isinstance(height, int):
            raise TypeError('height must be an integer')
        if height < 0:
            raise ValueError('height must be >= 0')
        self.__height = height

    @property
    def width(self):
        """return the value of width"""
        return self.__width

    @property
    def hieght(self):
        """return the value of hieght"""
        return self.__height

    @width.setter
    def width(self, value):
        """sets the width of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @hieght.setter
    def height(self, value):
        """sets the height of a rectangle"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise   ('height must be >= 0')
        self.__height = value
