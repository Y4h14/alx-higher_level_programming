#!/usr/bin/python3
"""defines a funciton that serialize Json"""
import json


def to_json_string(my_obj):
    """convert a stirng to a json"""
    return (json.dumps(my_obj))
