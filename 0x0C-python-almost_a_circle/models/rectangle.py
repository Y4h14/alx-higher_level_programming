#!/usr/bin/python3
"""define a rectagnle class"""
from base import Base


class Rectangle(Base):
    """define a rectangle object"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        intitalize a rectangle instance
        Args:
            -width (int): the width of the rectangle
            -height (int): the height of the rectangle
            -x (int): some x
            -y (int): some y
        """
        self.id = id

        if not isinstance(width, (int, float)):
            raise TypeError('width must be an integer')
        else:
            if width <= 0:
                raise ValueError('width must be > 0')
            else:
                self.__width = width

        if not isinstance(height, (int, float)):
            raise TypeError('height must be an integer')
        else:
            if height <= 0:
                raise ValueError('height must be > 0')
            else:
                self.__height = height

        if not isinstance(x, (int, float)):
            raise TypeError('x must be an integer')
        else:
            if x < 0:
                raise ValueError('x must be >= 0')
            else:
                self.__x = x

        if not isinstance(y, (int, float)):
            raise TypeError('y must be an integer')
        else:
            if y < 0:
                raise ValueError('y must be >= 0')
            else:
                self.__y = y

        super().__init__(id)

    @property
    def width(self):
        """sets the width value"""
        return self.__width

    @property
    def height(self):
        """sets the height value"""
        return self.__height

    @property
    def x(self):
        """sets the x value"""
        return self.__x

    @property
    def y(self):
        """sets the width value"""
        return self.__y

    @width.setter
    def width(self, value):
        """sets the width Value"""
        if not isinstance(value, (int, float)):
            raise TypeError('width must be an integer')
        else:
            if value <= 0:
                raise ValueError('width must be > 0')
            else:
                self.__width = value

    @height.setter
    def height(self, value):
        """sets the height Value"""
        if not isinstance(value, (int, float)):
            raise TypeError('height must be an integer')
        else:
            if value <= 0:
                raise ValueError('height must be > 0')
            else:
                self.__height = value

    @x.setter
    def x(self, value):
        """sets the x Value"""
        if not isinstance(value, (int, float)):
            raise TypeError('x must be an integer')
        else:
            if value < 0:
                raise ValueError('x must be >= 0')
            else:
                self.__x = value

    @y.setter
    def y(self, value):
        """sets the width Value"""
        if not isinstance(value, (int, float)):
            raise TypeError('y must be an integer')
        else:
            if value < 0:
                raise ValueError('y must be >= 0')
            else:
                self.__y = value

    def area(self):
        """calculate the area of a rectangle"""
        return (self.__width * self.__height)

    def display(self):
        for i in range(self.__y):
            print()
        for i in range(self.__height):
            print(self.__x * " " + self.__width * "#")

    def __str__(self):
        result = f"[Rectangle] ({self.id}) {self.__x}/{self.__y}"
        result += f" - {self.__width}/{self.__height}"
        return result

    def update(self, *args, **kwargs):
        """update rectangle attributes"""
        if args and len(args) != 0:
            attr = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                try:
                    setattr(self, attr[i], args[i])
                except KeyError:
                    return
        else:
            for key, value in kwargs.items():
                try:
                    setattr(self, key, value)
                except KeyError:
                    return

    def to_dictionary(self):
        """return the dictionary representation"""
        return {'id': self.id,
                'width': self.__width,
                'height': self.__height,
                'x': self.__x,
                'y': self.__y
                }
