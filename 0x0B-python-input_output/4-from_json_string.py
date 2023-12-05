#!/usr/bin/python3
"""define a funciont that deserialize json"""
import json


def from_json_string(my_str):
    """reurn an object from a JSON string"""
    return (json.loads(my_str))
