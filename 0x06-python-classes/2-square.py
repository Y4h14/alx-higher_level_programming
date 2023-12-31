#!/usr/bin/python3
"""defie a class of squares"""


class Square:
    """square with private instace attribute size"""
    def __init__(self, size=0):
        """
        Initilize a square object

        parameters:
        - size (int): size of the square
        """
        if type(size) is not int:
            raise TypeError('size must be an integer')

        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
