#!/usr/bin/python3
"""define a square class"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """a class for squares"""
    def __init__(self, size):
        """the init function"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
