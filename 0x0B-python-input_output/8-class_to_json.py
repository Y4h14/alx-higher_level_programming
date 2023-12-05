#!/usr/bin/python3
"""define a function to get the dictionary discription"""


def class_to_json(obj):
    """return dictionary discription with simple data structrue"""
    return (obj.__dict__)
