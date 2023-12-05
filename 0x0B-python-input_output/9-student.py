#!/usr/bin/python3
"""define a student class"""


class Student:
    """defines a student"""
    def __init__(self, first_name, last_name, age):
        """init function"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """retrives a dictionary representation of an instance"""
        return self.__dict__
