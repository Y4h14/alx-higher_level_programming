#!/usr/bin/python3
"""define a class for squares"""


class Square:
    """class of squares"""

    def __init__(self, size) -> None:

        """
        Initialzie a square with a given size

        parameters:
        - size (int): the size of the square
        """
        self.__size = size
