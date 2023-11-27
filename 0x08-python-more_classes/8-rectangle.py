#!/usr/bin/python3
"""define a rectangle class"""


class Rectangle:
    """ defines a rectangle object"""

    number_of_instances = 0
    print_symbol = "#"

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
        Rectangle.number_of_instances += 1

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
            raise ValueError('height must be >= 0')
        self.__height = value

    def __del__(self):
        """called when an object is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def __repr__(self):
        """return string representaiton used to recreate the object"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __str__(self):
        result = ""
        if self.__height == 0 or self.__width == 0:
            return result
        else:
            for i in range(self.__height):
                result += str(self.print_symbol) * self.__width
                if i != self.height - 1:
                    result += '\n'
            return (result)

    def area(self):
        """return the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the perimeter of a rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return (2 * (self.__height + self.__width))

    def bigger_or_equal(rect_1, rect_2):
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if Rectangle.area(rect_1) >= Rectangle.area(rect_2):
            return rect_1
        else:
            return rect_2
