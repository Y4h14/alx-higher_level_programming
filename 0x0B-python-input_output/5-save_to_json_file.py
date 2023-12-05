#!/usr/bin/python3
"""define a funciton that write serialized json to a file"""
import json


def save_to_json_file(my_obj, filename):
    """write an ovbject to a text file using JSON representation"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(json.dumps(my_obj)))
