#!/usr/bin/python3
"""defines a class"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """retrives a dictionary representation of an instance"""
        if attrs:
            new = {}
            for a in attrs:
                try:
                    new[a] = self.__dict__[a]
                except FileNotFoundError:
                    pass
            return new
        else:
            return self.__dict__
