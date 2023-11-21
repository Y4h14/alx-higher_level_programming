#!/usr/bin/python3
"""define a square class"""


class Square:
    """define a square"""
    def __init__(self, size=0):
        """
        Initilize a square
        Args:
            - size (int): size of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """calculates the area of a square"""
        return (self.__size ** 2)
