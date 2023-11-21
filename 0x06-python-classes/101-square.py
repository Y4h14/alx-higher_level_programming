#!/usr/bin/python3
"""define a class of squares"""


class Square:
    """define a square"""
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a Square object
        Args:
        - size (int): the size of the square
        - posisiton (tuple): the position of the square
        """
        if type(size) is int:
            if size < 0:
                raise ValueError('size must be >= 0')
            else:
                self.__size = size
        else:
            raise TypeError('size must be an integer')

        if not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    def area(self):
        """return the area of a square"""
        return self.__size ** 2

    def __str__(self):
        """"Print() represenation for the object"""
        result = ""
        if self.__size == 0:
            result += "\n"
        for i in range(self.__position[1]):
            result += "\n"
        for j in range(self.__size):
            if j == self.__size - 1:
                result += " " * self.__position[0] + "#" * self.__size
            else:
                result += " " * self.__position[0] + "#" * self.__size + "\n"
        return (result)

    def my_print(self):
        """function that prints a square"""
        temp = self.__position[1]
        if self.__size == 0:
            print()
        for i in range(self.__position[1]):
            print()
        for j in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

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

    @property
    def postition(self):
        """return the value of the postition"""
        return self.__position

    @postition.setter
    def position(self, position):
        """set the position attribute for the square object"""

        if not isinstance(position, tuple) or len(position) != 2 or \
                not all(isinstance(i, int) and i >= 0 for i in position):
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position
