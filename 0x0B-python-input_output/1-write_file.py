#!/usr/bin/python3
"""define a function to write in a file"""


def write_file(filename="", text=""):
    """write a string to a text file"""
    with open(filename, 'w', encoding="utf-8") as f:
        return (f.write(text))
