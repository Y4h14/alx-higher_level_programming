#!/usr/bin/python3
"""define a fucntion that append content to a file"""


def append_write(filename="", text=""):
    """append text to a file"""
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
