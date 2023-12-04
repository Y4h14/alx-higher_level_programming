#!/usr/bin/python3
"""define a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class for squares"""
    def __init__(self, size):
        """the init function"""
        super().__init__(size, size)
        self.integer_validator("square size", size)
        self.__size = size

    def area(self):
        """calculate the area of a square"""
        return (self.__size ** 2)
