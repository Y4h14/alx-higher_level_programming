#!/usr/bin/python3
"""define a class of squares"""


class Square:
    """define a square"""
    def __init__(self, size=0):
        """
        Initialize a Square object
        Args:
        - size (int): the size of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

    def area(self):
        """return the area of a square"""
        return self.__size ** 2

    def my_print(self):
        """function that prints a square"""
        if self.__size == 0:
            print()
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                print("#", end='')
            print()

    @property
    def size(self):
        """return the value of the size"""
        return self.__size

    @size.setter
    def size(self, size):
        """set the size attribute for the square object"""

        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')
