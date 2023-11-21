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

    def __eq__(self, other):
        """check if two objects are equal"""
        if self.area() == other.area():
            return True
        else:
            return False

    def __ne__(self, other):
        """check if two objects are not equal"""
        if self.area() != other.area():
            return True
        else:
            return False

    def __lt__(self, other):
        """compare two objects with less than"""
        if self.area() < other.area():
            return True
        else:
            return False

    def __gt__(self, other):
        """compare two objects with greater than"""
        if self.area() > other.area():
            return True
        else:
            return False

    def __le__(self, other):
        """compare two objects with less than or equal"""
        if self.area() <= other.area():
            return True
        else:
            return False

    def __ge__(self, other):
        """compare two objects with greater than or equal"""
        if self.area() >= other.area():
            return True
        else:
            return False
