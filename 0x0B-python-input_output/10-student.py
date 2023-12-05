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
        if type(attrs) == list and\
                all(type(a) == str for a in attrs):
            return ({k: getattr(self, k)
                    for k in attrs if hasattr(self, k)})
        else:
            return (self.__dict__)
