#!/usr/bin/python3
"""defines a square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """defines a square object"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        result = f"[Square] ({self.id}) {self.x}/{self.y}"
        result += f" - {self.width}"
        return result

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        if not isinstance(value, (int, float)):
            raise TypeError('width must be an integer')
        else:
            if value <= 0:
                raise ValueError('width must be > 0')
            else:
                self.width = value
                self.height = value

    def update(self, *args, **kwargs):
        """update squate instance"""
        if args and len(args):
            attr = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                try:
                    setattr(self, attr[i], args[i])
                except IndexError:
                    return
        else:
            try:
                for key, value in kwargs.items():
                    setattr(self, key, value)
            except KeyError:
                return

    def to_dictionary(self):
        return {'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
